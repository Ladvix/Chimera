import requests
import importlib
from pyrogram import Client, filters


def launch(bot, module_name):
    insult_generator = importlib.import_module(f'userbot.modules.{module_name}.insult_generator')

    @bot.app.on_message(filters.command('generate_insult', prefixes='.') & filters.me)
    def generate_insult(client, message):
        data = message.text.split(' ', maxsplit=2)
        count = int(data[1])

        message.delete()

        for i in range(0, count):
            bot.app.send_message(message.chat.id, insult_generator.genins())