import os
import config
import importlib
from utils import dirs, json_helper, credentials, console_color
from pyrogram import Client, filters, errors, utils
from userbot.commands.start import start
from userbot.commands.help import help
from userbot.commands.modules import modules
from userbot.commands.install import install
from userbot.commands.uninstall import uninstall


SESSION_NAME = 'session'

class userbot:

    def __init__(self):
        with open(dirs.ABS_PATH + 'banner.txt') as f:
            console_color.fore_fromhex('\n' + f.read() + '\n', '#FF4C2D')
        
        if True == (os.path.isfile(credentials.CREDENTIALS_PATH)):
            try:
                self.app = Client(SESSION_NAME)

            except Exception as e:
                console_color.fore_fromhex('Неизвестная ошибка: ' + str(e) + '\n', '#FF381E')
        else:
            config.API_ID = input('Введите API ID: ')
            config.API_HASH = input('Введите API Hash: ')
            config.PHONE_NUMBER = input('Введите ваш номер телефона: ')

            credentials.save(config.API_ID, config.API_HASH, config.PHONE_NUMBER)

            try:
                self.app = Client(SESSION_NAME, api_id=config.API_ID, api_hash=config.API_HASH)
                self.app.connect()

                sent_code = self.app.send_code(phone_number=config.PHONE_NUMBER)

                config.PHONE_CODE_HASH = sent_code.phone_code_hash
                config.PHONE_CODE = input('Введите код подтверждения: ')

                self.app.sign_in(phone_number=config.PHONE_NUMBER, phone_code=config.PHONE_CODE, phone_code_hash=config.PHONE_CODE_HASH)

                self.app.disconnect()

            except Exception as e:
                console_color.fore_fromhex('Неизвестная ошибка: ' + str(e) + '\n', '#FF381E')


    def add_handlers(self):
        @self.app.on_message(filters.command('start', prefixes='.') & filters.me)
        def start_handler(client, message):
            start.init(client, message)

        @self.app.on_message(filters.command('help', prefixes='.') & filters.me)
        def help_handler(client, message):
            help.init(client, message)

        @self.app.on_message(filters.command('modules', prefixes='.') & filters.me)
        def modules_handler(client, message):
            modules.init(client, message)

        @self.app.on_message(filters.command('install', prefixes='.') & filters.me)
        def install_handler(client, message):
            install.init(client, message)

        @self.app.on_message(filters.command('uninstall', prefixes='.') & filters.me)
        def uninstall_handler(client, message):
            uninstall.init(client, message)


    def launch_modules(self):
        if False == (os.path.isdir(dirs.MODULES_PATH)):
            os.makedirs(os.path.isdir(dirs.MODULES_PATH))

        for module_name in [f for f in os.listdir(dirs.MODULES_PATH) if os.path.isdir(os.path.join(dirs.MODULES_PATH, f)) and f != 'pycache']:
            try:
                os.system(f'pip install -r userbot/modules/{module_name}/requirements.txt --quiet')
                importlib.import_module(f'userbot.modules.{module_name}.main').launch(self, module_name)
            except Exception as e:
                console_color.fore_fromhex('Неизвестная ошибка: ' + str(e) + '\n', '#FF381E')


    def launch_bot(self):
        print('Запуск бота...')
        
        try:
            self.app.run()
        
        except (errors.AuthKeyUnregistered, AttributeError):
            os.remove(credentials.CREDENTIALS_PATH)
            console_color.fore_fromhex('Произошла непредвиденная ошибка. Перезапустите программу' + '\n', '#FF381E')

        except Exception as e:
            console_color.fore_fromhex('Неизвестная ошибка: ' + str(e) + '\n', '#FF381E')
