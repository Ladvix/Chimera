import os
import time
from utils import dirs

def init(client, message):
    with open(dirs.COMMANDS_PATH + 'modules/templates/README.html', encoding='utf-8') as f:
        output = f.read()

        for module_name in [f for f in os.listdir(dirs.MODULES_PATH) if os.path.isdir(os.path.join(dirs.MODULES_PATH, f)) and f != 'pycache']:
            output = output + f'\n<emoji id="5416117059207572332">▫</emoji> <b>{module_name}</b>'

        message.edit(output + '\nㅤ')