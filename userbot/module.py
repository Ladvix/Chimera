import os
import importlib


def launch(bot, module_name):
    os.system(f'pip install -r userbot/modules/{module_name}/requirements.txt --quiet')
    importlib.import_module(f'userbot.modules.{module_name}.main').launch(bot, module_name)