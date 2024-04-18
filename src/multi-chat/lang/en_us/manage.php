<?php

return [
    'route' => 'Manage',
    'interface.header' => 'Management Interface',
    'button.delete' => 'Delete',
    'button.update' => 'Update',
    'button.create' => 'Create',
    'button.save' => 'Save',
    'button.yes' => "Yes, I'm sure",
    'button.no' => 'No, cancel',
    'button.cancel' => 'Cancel',
    'button.close' => 'Close',
    'button.accept' => 'I accepted',

    //Tabs
    'tab.groups' => 'Groups',
    'tab.users' => 'Users',
    'tab.llms' => 'Models',
    'tab.settings' => 'Settings',

    //Groups
    'button.new_group' => 'New Group',
    'header.create_group' => 'Create a new Group',
    'label.tab_permissions' => 'Tab Permissions',
    'label.invite_code' => 'Invite Token',
    'label.group_name' => 'Name',
    'label.invite_code' => 'Invite Code',
    'placeholder.invite_code' => 'Invite Code',
    'label.describe' => 'Describe',
    'placeholder.group_name' => 'Group name',
    'placeholder.group_detail' => 'Details for the group',
    'label.read' => 'Read',
    'label.delete' => 'Delete',
    'label.update' => 'Update',
    'label.llm_permission.disabled' => 'Model Permissions (Disabled LLM)',
    'label.llm_permission.enabled' => 'Model Permissions (Enabled LLM)',
    'header.edit_group' => 'Edit group',
    'hint.group_updated' => 'Group Updated!',
    'hint.group_created' => 'Group Created!',
    'modal.delete_group.header' => 'Are you sure you want to delete group',

    //Users
    'header.menu' => 'Menu',
    'header.group_selector' => 'Group Selector',
    'header.fuzzy_search' => 'Fuzzy Search',
    'header.create_user' => 'Create User',
    'label.group_selector' => 'List the group users to manage specific user',
    'label.fuzzy_search' => 'Search the user by Email or Name',
    'label.create_user' => 'Create a new User profile',

    'create_user.header' => 'Create a new User',
    'create_user.joined_group' => 'Joined Group',
    'label.members' => 'Members',
    'label.other_users' => 'Other Users',
    'button.return_group_list' => 'Return to Group List',
    'placeholder.search_user' => 'Search Email or Name',
    'hint.enter_to_search' => 'Press enter to search',

    'group_selector.header' => 'Edit User',
    'placeholder.email' => "the user's Email",
    'placeholder.username' => 'Username',
    'label.name' => 'Name',
    'modal.delete_user.header' => 'Are you sure you want to delete user',
    'label.email' => 'Email',
    'label.password' => 'Password',
    'label.update_password' => 'Update Password',
    'label.detail' => 'Detail',
    'placeholder.new_password' => 'New Password',
    'label.require_change_password' => 'Require to change password when login',
    'label.extra_setting'=>'Extra Settings',
    'label.created_at'=>"Created At",
    'label.updated_at'=>'Updated At',

    //LLMs
    'button.new_model' => 'New Model',
    'label.enabled_models' => 'Enabled Models',
    'label.disabled_models' => 'Disabled Models',
    'header.create_model' => 'Create Model Profile',
    'modal.create_model.header' => 'Are you sure you want to CREATE this Model Profile?',
    'label.model_image' => 'Model Image',
    'label.model_name' => 'Model Name',
    'label.order' => 'Order',
    'label.link' => 'Link',
    'placeholder.description' => 'Description for this Model',
    'label.version' => 'Version',
    'label.access_code' => 'Access Code',
    'placeholder.link' => 'Link for more information to this Model',
    'header.update_model' => 'Modify Model Profile',
    'label.description' => 'Description',
    'modal.update_model.header' => 'Are you sure you want to UPDATE this LLM Profile?',
    'modal.delete_model.header' => 'Are you sure you want to DELETE this LLM Profile?',

    //setting
    'header.settings' => 'System Settings',
    'label.settings' => 'All the system settings here',
    'label.agent_API' => 'Agent API Location',
    'label.allow_register' => 'Allow Register',
    'button.reset_redis' => 'Reset Redis Caches',
    'hint.saved' => 'Saved.',
    'hint.redis_cache_cleared' => 'Redis Cache Cleared.',
    'label.need_invite' => 'Register Need Invite',
    'label.footer_warning' => 'Footer Warning',
    'label.safety_guard_API' => 'Safety Guard Location',
    'label.anno' => 'Announcement',
    'label.tos' => 'Terms of Service',

    //Permissions
    'perm.Room_update_import_chat' => 'Import Chat',
    'perm.Room_update_new_chat' => 'Create New Chat',
    'perm.Room_update_feedback' => 'Giving feedback',
    'perm.Room_update_send_message' => 'Sending Message',
    'perm.Room_update_react_message' => 'React Buttons',
    'perm.Room_read_export_chat' => 'Export Chat',
    'perm.Room_delete_chatroom' => 'Delete Chatroom',
    'perm.Room_update_upload_file' => 'Upload File',
    'perm.Chat_update_react_message' => 'React Buttons',
    'perm.Dashboard_read_statistics' => 'Statistics',
    'perm.Dashboard_read_blacklist' => 'Blacklist',
    'perm.Dashboard_read_feedbacks' => 'Feedbacks',
    'perm.Dashboard_read_logs' => 'Logs',
    'perm.Dashboard_read_safetyguard' => 'Safety Guard',
    'perm.Dashboard_read_inspect' => 'Inspect',
    'perm.Chat_update_detail_feedback' => 'Detail Feedback',
    'perm.Room_update_detail_feedback' => 'Detail Feedback',
    'perm.Chat_update_send_message' => 'Sending Message',
    'perm.Chat_update_new_chat' => 'Create New Chat',
    'perm.Chat_update_upload_file' => 'Upload File',
    'perm.Chat_update_feedback' => 'Giving feedback',
    'perm.Chat_update_import_chat' => 'Import Chat',
    'perm.Chat_read_access_to_api' => 'Use API',
    'perm.Chat_read_export_chat' => 'Export Chat',
    'perm.Chat_delete_chatroom' => 'Delete Chatroom',
    'perm.Profile_update_api_token' => 'Update Web API Token',
    'perm.Profile_update_name' => 'Update Username',
    'perm.Profile_update_email' => 'Update Email',
    'perm.Profile_update_password' => 'Update Password',
    'perm.Profile_update_external_api_token' => 'Update External API Token',
    'perm.Profile_read_api_token' => 'Read Web API Token',
    'perm.Profile_delete_account' => 'Delete Account',

    'perm.Chat_update_detail_feedback.describe' => 'Permission to give detailed feedbacks',
    'perm.Room_update_detail_feedback.describe' => 'Permission to give detailed feedbacks',
    'perm.Profile_update_name.describe' => 'Permission to update name',
    'perm.Profile_update_email.describe' => 'Permission to update email',
    'perm.Profile_update_password.describe' => 'Permission to update password',
    'perm.Profile_update_external_api_token.describe' => 'Permission to update External API Token',
    'perm.Profile_read_api_token.describe' => 'Permission to read Kuwa Chat API token',
    'perm.Profile_delete_account.describe' => 'Permission to delete their account',
    'perm.Profile_update_api_token.describe' => 'Permission to update Kuwa Chat API token',
    'perm.Chat_read_access_to_api.describe' => 'Permission to use chat API',
    'perm.Chat_update_send_message.describe' => 'Permission to send message in chat',
    'perm.Room_update_send_message.describe' => 'Permission to send message in room',
    'perm.Chat_update_new_chat.describe' => 'Permission to create new chat',
    'perm.Room_update_new_chat.describe' => 'Permission to create new chat',
    'perm.Chat_update_upload_file.describe' => 'Permission to upload file',
    'perm.Room_update_upload_file.describe' => 'Permission to upload file',
    'perm.Chat_update_feedback.describe' => 'Permission to use feedback',
    'perm.Room_update_feedback.describe' => 'Permission to use feedback',
    'perm.Room_delete_chatroom.describe' => 'Permission to delete chatroom',
    'perm.Chat_delete_chatroom.describe' => 'Permission to delete chatroom',
    'perm.Chat_read_export_chat.describe' => 'Permission to export chat history',
    'perm.Room_read_export_chat.describe' => 'Permission to export chat history',
    'perm.Chat_update_import_chat.describe' => 'Permission to import history',
    'perm.Room_update_import_chat.describe' => 'Permission to import history',
    'perm.Chat_update_react_message.describe' => 'Permission to use extra react buttons',
    'perm.Room_update_react_message.describe' => 'Permission to use extra react buttons',
    'perm.Dashboard_read_statistics.describe' => 'Permission to access statistics tab',
    'perm.Dashboard_read_blacklist.describe' => 'Permission to access blacklist tab',
    'perm.Dashboard_read_feedbacks.describe' => 'Permission to access feedbacks tab',
    'perm.Dashboard_read_logs.describe' => 'Permission to access logs tab',
    'perm.Dashboard_read_safetyguard.describe' => 'Permission to access safetyguard tab',
    'perm.Dashboard_read_inspect.describe' => 'Permission to inspect tab',
];
