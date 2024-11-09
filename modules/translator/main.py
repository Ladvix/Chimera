import json
from pyrogram import Client, filters
from googletrans import Translator, LANGUAGES
TRANSLATOR = Translator()

def init(app):

    @app.on_message(filters.command('tnt', prefixes = '.') & filters.me)
    def _(client, message):

        output = ''

        data = message.text.split(' ', maxsplit = 2)
        text = data[2]
        dest = data[1]

        translation = TRANSLATOR.translate(text, dest = dest)

        output = translation.text

        message.edit_text(output)