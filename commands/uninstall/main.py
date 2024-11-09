import os, requests, zipfile, shutil
import utils.dirs, utils.module_init

def response(client, message, app):

    text = message.text.split(' ', maxsplit = 4)
    module_name = text[1]

    with open(f'{utils.dirs.COMMANDS_PATH}uninstall/waiting.html', encoding='utf-8') as f:
        message_text = f.read()
        message.edit_text(message_text)

    try:
        shutil.rmtree(utils.dirs.ABS_PATH + '/modules/' + module_name)

        with open(f'{utils.dirs.COMMANDS_PATH}uninstall/success.html', encoding='utf-8') as f:
            message_text = f.read()
            message.edit_text(message_text)

    except Exception as e:
        message.edit_text('<b>ㅤ\n' + str(e) + '\nㅤ</b>')