from userbot import chimera


if __name__ == '__main__':
    # Авторизация и запуск юзербота
    bot = chimera.userbot()
    bot.add_handlers()
    bot.launch_modules()
    bot.launch_bot()