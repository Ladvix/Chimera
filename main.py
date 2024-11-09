import os
import utils.module_init
import config, utils.terminal_effects
import commands.help.main as _HELP_
import commands.install.main as _INSTALL_
import commands.uninstall.main as _UNINSTALL_
import commands.modules.main as _MODULES_
from pyrogram import Client, filters

utils.terminal_effects.on_start()

app = Client('my_account', api_id = config.API_ID, api_hash = config.API_HASH, phone_number = config.PHONE_NUMBER)

for module_name in [f for f in os.listdir('modules') if os.path.isdir(os.path.join('modules', f)) and f != 'pycache']:
    utils.module_init.INIT(app, module_name)

# Основные команды
@app.on_message(filters.command('help', prefixes = '.') & filters.me)
def _(client, message): _HELP_.response(client, message, app)

@app.on_message(filters.command('install', prefixes = '.') & filters.me)
def _(client, message): _INSTALL_.response(client, message, app)

@app.on_message(filters.command('uninstall', prefixes = '.') & filters.me)
def _(client, message): _UNINSTALL_.response(client, message, app)

@app.on_message(filters.command('modules', prefixes = '.') & filters.me)
def _(client, message): _MODULES_.response(client, message, app)

@app.on_message(filters.me)
def _(client, message):

    pass #print(message)

app.run()