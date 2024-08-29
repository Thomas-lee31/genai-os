import os
import sys
import asyncio
import logging
import json

from kuwa.executor import LLMExecutor, Modelfile
from kuwa.client import KuwaClient
from kuwa.executor.modelfile import ParameterDict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import taskPrompt

logger = logging.getLogger(__name__)

class GongwenExecutor(LLMExecutor):
    def __init__(self):
        super().__init__()

    def extend_arguments(self, parser):
        """
        Override this method to add custom command-line arguments.
        """
        generator_group = parser.add_argument_group('Generator Options')
        generator_group.add_argument('--api_base_url', default="http://127.0.0.1/", help='The API base URL of Kuwa multi-chat WebUI')
        generator_group.add_argument('--api_key', default=None, help='The API authentication token of Kuwa multi-chat WebUI')
        generator_group.add_argument('--limit', default=3072, type=int, help='The limit of the LLM\'s context window')
        generator_group.add_argument('--model', default='taide', help='The model name (access code) on Kuwa multi-chat WebUI')
        
        parser.add_argument('--delay', type=float, default=0.02, help='Inter-token delay')

    def setup(self):
        pass
        
    def _app_setup(self, params:ParameterDict=ParameterDict()):
        general_params = params["_"]
        generator_params = params["generator_"]
        self.stop = False
        self.client = KuwaClient(
                base_url = "http://localhost",
                kernel_base_url="http://localhost:9000",
                model = generator_params.get("model", self.args.model),
                auth_token=general_params.get("user_token", self.args.api_key),

            )
       
    async def callForResponse(self, inputMsg, client):
        async for chunk in client.chat_complete(messages=inputMsg, timeout=1200):
            if self.stop:
                logger.info(f"\033[31mStop Response for {client.model}\033[0m")
                # self.stop = False 下面也都不要生成了
                yield "<font color='red'>"
                yield "\n# 您已經中斷生成\n"
                yield "</font>"
                break
            yield chunk
            
        logger.info(f"\033[92m{client.model} Finish\033[0m")

    async def taskMustWrite(self, userInput):
        stageName = "# 摘錄"
        yield f"\n{stageName}\n"
        
        msg = taskPrompt.mustWrite(userInput)
        messages = [
            {"role": "user", "content": msg}
        ]
        self.mustWrite = ""
        async for response in self.callForResponse(messages, self.client):
            self.mustWrite += response
            yield response
    
    async def taskExpand(self, userInput):
        stageName = "# 擴寫"
        yield f"\n{stageName}\n"
        msg = taskPrompt.expand(userInput)
        messages = [
            {"role": "user", "content": msg}
        ]
        
        self.expandOut = ""
        async for response in self.callForResponse(messages, self.client):
            self.expandOut += response
            yield response

    async def taskTopic(self):
        stageName = "# 主旨產生"
        yield f"\n{stageName}\n"
        msg = taskPrompt.topic(self.expandOut)
        messages = [
            {"role": "user", "content": msg}
        ]
        
        self.mainTopic = ""
        async for response in self.callForResponse(messages, self.client):
            self.mainTopic += response
            yield response

    async def taskInfo(self):
        stageName = "# 說明產生"
        yield f"\n{stageName}\n"
        msg = taskPrompt.info(self.expandOut)
        messages = [
            {"role": "user", "content": msg}
        ]
        
        self.info = ""
        async for response in self.callForResponse(messages, self.client):
            self.info += response
            yield response
    
    async def taskFormat(self):
        stageName = "# 公文用語轉換"
        yield f"\n{stageName}\n"

        msg = taskPrompt.format(self.mainTopic, self.info)
        logger.info(msg)
        messages = [
            {"role": "user", "content": msg}
        ]
        
        formation = ""
        async for response in self.callForResponse(messages, self.client):
            formation += response
            yield response
        
    async def llm_compute(self, history: list[dict], modelfile:Modelfile):
        try:
            self._app_setup(params=modelfile.parameters)

            logger.info('\033[92mGongwen Start!\033[0m')

            userInput = history[-1]['content'].strip()
            userId    = modelfile.parameters.get('_user_id', 'unknown')
            
            self.chse = -1
            if os.path.exists(f"chse_user{userId}.txt"):
                with open(f"chse_user{userId}.txt", "r") as f:
                    self.chse = f.read().strip()

            if "沒事" in userInput:
                yield "沒事就不要找我啦，討厭 >///<"
                return
            
            elif self.chse in ['1', '2', '3', '4', '5']:
                self.chse = int(self.chse)
                with open(f"chse_user{userId}.txt", "w") as f:
                    f.write('fin')
            elif userInput not in ['1', '2', '3', '4', '5']:
                yield """《公文產生》
                請輸入1-5選擇功能:
                1 - 執行所有步驟 *(改寫、產生主旨、產生說明、用語轉換)*
                2 - 改寫
                3 - 產生主旨
                4 - 產生說明
                5 - 公文用語轉換"""

                with open(f"chse_user{userId}.txt", "w") as f:
                    f.write('wrong input')
                return
            else:
                options = {
                    '1' : "請提供你的內容，我會幫你執行所有步驟。\n*(改寫、產生主旨、產生說明、用語轉換)*",
                    '2' : "請簡單描述你的想法，我會幫你「改寫」成完整的文章。",
                    '3' : "請提供一篇完整的文章，我會幫你產生「主旨」。",
                    '4' : "請提供一篇完整的文章，我會幫你產生「說明」。",
                    '5' : """請提供具有「主旨」以及「說明」的文章，我會幫你將其轉換為「公文用語」。\n*範例: 以便->俾*"""
                }
                yield options[userInput]
                yield "\n\n*...輸入\'/n\'取消這次服務...*"
                with open(f"chse_user{userId}.txt", "w") as f:
                    f.write(userInput)
                return

            if userInput == "/n":
                yield "好的，已經取消服務。"
                return
            # ================== 以下為主要流程 ==================
            task_map = {  # 0: 整個流程, 1: 擴寫, 2: 產生主旨, 3: 產生說明, 4: 公文格式化
                1: [lambda: self.taskExpand(userInput), lambda: self.taskTopic(), lambda: self.taskInfo(), lambda: self.taskFormat()], 
                2: [lambda: self.taskExpand(userInput)],                                                                               
                3: [lambda: self.taskTopic()],                                                                                         
                4: [lambda: self.taskInfo()],                                                                                            
                5: [lambda: self.taskFormat()]                                                                                         
            }

            # 把userInput作為中間產物傳入
            if self.chse == 3: # 只產生主旨
                self.expandOut = userInput
                self.test = True
            elif self.chse == 4:
                self.expandOut = userInput
            elif self.chse == 5:
                self.mainTopic = userInput
                self.info = ""

            
            for task in task_map[self.chse]:
                async for response in task():
                    yield response
                
                yield "\n\n---\n\n"
                
            
        except Exception as e:
            logger.exception("Error occurs during generation.")
            yield str(e)
        finally:
            logger.info('\033[92m [Gongwen DONE]\n\033[0m')
            logger.debug("finished")

    async def abort(self):
        self.stop = True
        logger.debug("aborted")
        return "Aborted"


if __name__ == "__main__":
    executor = GongwenExecutor()
    executor.run()
    