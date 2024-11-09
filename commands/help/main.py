import os, sys
import utils.dirs

def response(client, message, app):

    data = message.text.split(' ', maxsplit = 1)
    if len(data) == 1:
        path = f'{utils.dirs.COMMANDS_PATH}help/'
    else:
        path = f'{utils.dirs.MODULES_PATH}{data[1]}/'

    try:
        with open(f'{path}help_message.html', encoding='utf-8') as f:
            message_text = f.read()
            message.edit_text(message_text)

    except:
        message.edit_text(f'<b><emoji id="5240241223632954241">🚫</emoji> Module "{data[1]}" was not found.</b>')