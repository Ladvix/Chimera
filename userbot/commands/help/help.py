import os
from utils import dirs
from string import Template


def init(bot, client, message):
    try:
        module_name = message.text.split(' ', maxsplit=1)[1]
        path = dirs.MODULES_PATH + f'{module_name}/templates/README.html'

        if True == (os.path.isfile(path)):
            with open(path, 'r', encoding='utf-8') as f:
                message.edit(f.read())
        else:
            with open(dirs.COMMANDS_PATH + '/help/templates/error.html', 'r', encoding='utf-8') as f:
                s = Template(f.read())
                message.edit(s.substitute(module_name=module_name))

    except Exception as e:
        pass