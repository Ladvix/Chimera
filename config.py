import os
import time
from utils import credentials, dirs, json_helper


try:
    data = json_helper.read(credentials.CREDENTIALS_PATH)
    API_ID = data['api_id']
    API_HASH = data['api_hash']
    PHONE_NUMBER = data['phone_number']

except FileNotFoundError:
    pass

PHONE_CODE = ''
PHONE_CODE_HASH = ''