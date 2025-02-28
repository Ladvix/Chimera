from pyrogram import Client, filters
from googletrans import Translator, LANGUAGES
TRANSLATOR = Translator()


def launch(bot, module_name):
    @bot.app.on_message(filters.command('tnt', prefixes='.') & filters.me)
    def tnt(client, message):
        data = message.text.split(' ', maxsplit=2)
        text = data[2]
        dest = data[1]

        message.edit_text(TRANSLATOR.translate(text, dest = dest).text)