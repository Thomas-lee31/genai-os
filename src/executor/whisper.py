import os
import re
import sys
import json
import asyncio
import logging
import requests
import tempfile
import queue
import mimetypes
from threading import Thread
from pywhispercpp.model import Model as WhisperModel
from pywhispercpp.utils import to_timestamp
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kuwa.executor import LLMExecutor

logger = logging.getLogger(__name__)

from pywhispercpp.model import Model


class WhisperExecutor(LLMExecutor):
    def __init__(self):
        super().__init__()

    def extend_arguments(self, parser):
        parser.add_argument('--model', default="large", help='The model name')
        parser.add_argument('--speedup', default=False, action="store_true", help='Pass the speedup argument to whisper.cpp.')
        parser.add_argument('--language', default=None, help='The language to detect.')

    def setup(self):
        if not self.LLM_name:
            self.LLM_name = "whisper"

        self.model = WhisperModel(
            self.args.model,
            language=self.args.language,
            print_progress=True,
            translate=False,
            log_level=self.log_level
        )
        self.speedup = self.args.speedup

        self.stop = False

    def extract_last_url(self, chat_history: list):
        """
        Find the latest URL provided by the user and trim the chat history to there.
        """

        url = None
        begin_index = 0
        user_records = list(filter(lambda x: not x["isbot"], chat_history))
        for i, record in enumerate(reversed(user_records)):

            urls_in_msg = re.findall(r'^(https?://[^\s]+)$', record["msg"])
            if len(urls_in_msg) != 0: 
                url = urls_in_msg[-1]
                begin_index = len(chat_history) - i - 1
                break
        
        return url, chat_history[begin_index:]

    def download(self, url):
        # Create a temporary file to store the downloaded content
        filepath = None
        response = requests.get(url)
        content_type = response.headers["Content-Type"]
        logger.debug(f"Content-Type: {content_type}")
        extension = mimetypes.guess_extension(content_type.split(';', 1)[0])
        with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as f:
            f.write(response.content)
            filepath = f.name
        return filepath
    
    async def transcribe(self, filepath):
        q = queue.Queue() # whisper produces, the generator consumes
        job_done = object() # signals the processing is done

        # Producer
        def on_new_segment(segments):
            for s in segments:
                q.put(s)
        def producer_task():
            self.model.transcribe(filepath, speed_up=self.speedup, new_segment_callback=on_new_segment)
            q.put(job_done)

        producer_thread = Thread(target=producer_task)
        producer_thread.start()

        # Consumer
        while True:
            try:
                next_item = q.get(block=False) # Blocks until an input is available
            except queue.Empty:
                continue
            if next_item is job_done:
                break
            yield next_item

        producer_thread.join()

    async def llm_compute(self, data):

        filepath = None
        try:
            self.stop = False
            chat_history = json.loads(data.get("input"))
            url, chat_history = self.extract_last_url(chat_history)
            if url is None: 
                raise ValueError("An URL to a audio file is expected.")

            filepath = self.download(url)

            result = self.transcribe(filepath=filepath)
            async for segment in result:
                yield "[{} ---> {}] {}\n".format(
                    to_timestamp(segment.t0), to_timestamp(segment.t1), segment.text
                )
                if self.stop: break
        except Exception as e:
            logger.exception("Error occurs during generation.")
            yield str(e)
        finally:
            self.stop = False
            if filepath is not None:
                os.remove(filepath)
            logger.debug("finished")

    async def abort(self):
        self.stop = True
        logger.debug("aborted")
        return "Aborted"

if __name__ == "__main__":
    executor = WhisperExecutor()
    executor.run()