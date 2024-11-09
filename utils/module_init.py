import os, sys, importlib
import utils.dirs

def INIT(app, module_name):
    
    path = f'{utils.dirs.MODULES_PATH}{module_name}/'
    os.system(f'pip install -r {path}requirements.txt --quiet')
    importlib.import_module(f'modules.{module_name}.main').init(app)