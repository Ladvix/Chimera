import os
import json


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
