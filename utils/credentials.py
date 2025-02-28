import time
from utils import dirs, json_helper


CREDENTIALS_PATH = dirs.ABS_PATH + 'credentials.json'


def save(api_id, api_hash, phone_number):
    json_helper.write(CREDENTIALS_PATH, 
    {
        'api_id': api_id or '',
        'api_hash': api_hash or '',
        'phone_number': phone_number or '',
        'time': int(time.time())
    })