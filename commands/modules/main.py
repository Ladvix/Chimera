import os
import utils.dirs

def response(client, message, app):

    output = ''

    for module_name in [f for f in os.listdir('modules') if os.path.isdir(os.path.join('modules', f)) and f != 'pycache']:
        output = f'{output}\n<emoji id="5416117059207572332">▫</emoji> {module_name}\n<code>.help {module_name}</code>\n'

    message.edit_text(output)