from utils import dirs, git
from string import Template


def format_url(url):
    url = url.endswith('.git') == True and url[:-4] or url
    new_url = f'{url}/archive/refs/heads/main.zip'

    return new_url


def init(client, message):
    data = message.text.split(' ', maxsplit=4)
    url = format_url(data[1])
    module_name = data[3]

    with open(f'{dirs.COMMANDS_PATH}install/templates/loading.html', encoding='utf-8') as f:
        message.edit(f.read())

    try:
        git.clone(url, dirs.MODULES_PATH + module_name)
        with open(dirs.COMMANDS_PATH + 'install/templates/success.html', encoding='utf-8') as f:
            s = Template(f.read())
            message.edit(s.substitute(module_name=module_name))

    except Exception as e:
        with open(dirs.COMMANDS_PATH + 'install/templates/error.html', encoding='utf-8') as f:
            s = Template(f.read())
            message.edit(s.substitute(error_message=str(e)))