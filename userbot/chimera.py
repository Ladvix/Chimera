import os
import sys
import config
import importlib
from pyrogram import Client, filters, errors, utils
from utils import dirs, json_helper, credentials, console_color
from userbot import module
from userbot.commands.start import start
from userbot.commands.help import help
from userbot.commands.modules import modules
from userbot.commands.install import install
from userbot.commands.uninstall import uninstall


SESSION_NAME = 'session'
SESSION_PATH = dirs.ABS_PATH + f'{SESSION_NAME}.session'

class userbot:

    def __init__(self):
        with open(dirs.ABS_PATH + 'banner.txt') as f:
            print('\n' + console_color.fore_fromhex(f.read(), hex_color='#FF4C2D') + '\n')
        
        console_color.print_log('Авторизация')

        if True == (os.path.isfile(credentials.CREDENTIALS_PATH)):
            try:
                print('  ↳ Загрузка существующей сессии...')
                self.app = Client(SESSION_NAME)
                print('  ↳ Сессия загружена успешно!')

            except Exception as e:
                console_color.print_error(f'Ошибка при загрузке сессии: {str(e)}')
                sys.exit(1)
        else:
            print('  ↳ Для работы бота необходимо ввести данные авторизации Telegram API')
            print()
            
            config.API_ID = console_color.print_input_prompt('Введите API ID: ')
            config.API_HASH = console_color.print_input_prompt('Введите API Hash: ')
            config.PHONE_NUMBER = console_color.print_input_prompt('Введите ваш номер телефона: ')

            credentials.save(config.API_ID, config.API_HASH, config.PHONE_NUMBER)

            try:
                self.app = Client(SESSION_NAME, api_id=config.API_ID, api_hash=config.API_HASH)
                self.app.connect()

                sent_code = self.app.send_code(phone_number=config.PHONE_NUMBER)

                config.PHONE_CODE_HASH = sent_code.phone_code_hash
                config.PHONE_CODE = console_color.print_input_prompt('Введите код подтверждения: ')

                try:
                    self.app.sign_in(phone_number=config.PHONE_NUMBER, phone_code=config.PHONE_CODE, phone_code_hash=config.PHONE_CODE_HASH)
                except errors.SessionPasswordNeeded:
                    password = console_color.print_input_prompt('Введите пароль от 2fa: ')
                    self.app.check_password(password)

                self.app.disconnect()

            except errors.BadRequest as e:
                try:
                    if hasattr(self, 'app') and self.app is not None:
                        self.app.disconnect()
                except:
                    pass
                    
                if 'API_ID_INVALID' in str(e):
                    os.remove(credentials.CREDENTIALS_PATH)
                    if os.path.isfile(SESSION_PATH):
                        os.remove(SESSION_PATH)
                    console_color.print_error('API ID или API Hash введены неверно')
                    sys.exit(1)
                else:
                    os.remove(credentials.CREDENTIALS_PATH)
                    if os.path.isfile(SESSION_PATH):
                        os.remove(SESSION_PATH)
                    console_color.print_error(f'Неизвестная ошибка: {str(e)}')
                    sys.exit(1)

            except Exception as e:
                try:
                    if hasattr(self, 'app') and self.app is not None:
                        self.app.disconnect()
                except:
                    pass
                    
                os.remove(credentials.CREDENTIALS_PATH)
                if os.path.isfile(SESSION_PATH):
                    try:
                        os.remove(SESSION_PATH)
                    except:
                        pass
                console_color.print_error(f'Неизвестная ошибка: {str(e)}')
                sys.exit(1)


    def add_handlers(self):
        @self.app.on_message(filters.command('start', prefixes='.') & filters.me)
        def start_handler(client, message):
            start.init(self, client, message)

        @self.app.on_message(filters.command('help', prefixes='.') & filters.me)
        def help_handler(client, message):
            help.init(self, client, message)

        @self.app.on_message(filters.command('modules', prefixes='.') & filters.me)
        def modules_handler(client, message):
            modules.init(self, client, message)

        @self.app.on_message(filters.command('install', prefixes='.') & filters.me)
        def install_handler(client, message):
            install.init(self, client, message)

        @self.app.on_message(filters.command('uninstall', prefixes='.') & filters.me)
        def uninstall_handler(client, message):
            uninstall.init(self, client, message)


    def launch_modules(self):
        if False == (os.path.isdir(dirs.MODULES_PATH)):
            os.makedirs(dirs.MODULES_PATH)

        print()
        console_color.print_log('Модули')
        
        modules_found = [f for f in os.listdir(dirs.MODULES_PATH) if os.path.isdir(os.path.join(dirs.MODULES_PATH, f)) and f != 'pycache']
        
        if not modules_found:
            print('  ↳ Модули не найдены')
            return
            
        print(f'  ↳ Найдено модулей: {len(modules_found)}')
        
        for module_name in modules_found:
            try:
                print(f'  ↳ Загрузка модуля "{module_name}"...')
                try:
                    module.launch(self, module_name)
                    print(f'  ↳ Модуль "{module_name}" загружен')
                except KeyboardInterrupt:
                    print()
                    return

            except Exception as e:
                console_color.print_error(f'Ошибка при загрузке модуля "{module_name}": {str(e)}')
                print()


    def launch_bot(self):
        print()
        console_color.print_log('Запуск')
        
        try:
            print('  ↳ Бот запущен и готов к работе!')
            print('  ↳ Нажмите Ctrl+C для остановки')
            print()
            self.app.run()
        
        except (errors.AuthKeyUnregistered, AttributeError):
            try:
                if hasattr(self, 'app') and self.app is not None:
                    self.app.disconnect()
            except:
                pass
                
            os.remove(credentials.CREDENTIALS_PATH)
            console_color.print_error('Произошла ошибка авторизации. Перезапустите программу')

        except KeyboardInterrupt:
            console_color.print_warning('Бот остановлен пользователем')

        except Exception as e:
            console_color.print_error(f'Неизвестная ошибка: {str(e)}')
