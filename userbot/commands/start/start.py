from utils import dirs

def init(bot, client, message):
    with open(dirs.COMMANDS_PATH + 'start/templates/README.html', 'r', encoding='utf-8') as f:
        message.edit(f.read())