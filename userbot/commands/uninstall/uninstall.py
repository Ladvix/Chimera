import shutil
from string import Template
from utils import dirs


def init(bot, client, message):
    data = message.text.split(' ', maxsplit=2)
    module_name = data[1]

    try:
        shutil.rmtree(dirs.MODULES_PATH + module_name)
        with open(dirs.COMMANDS_PATH + 'uninstall/templates/success.html', encoding='utf-8') as f:
            s = Template(f.read())
            message.edit(s.substitute(module_name=module_name))

    except Exception as e:
        with open(dirs.COMMANDS_PATH + 'uninstall/templates/error.html', encoding='utf-8') as f:
            s = Template(f.read())
            message.edit(s.substitute(error_message=str(e)))