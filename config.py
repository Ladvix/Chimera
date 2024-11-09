import os, time, json
import utils.dirs

# Проверка на существование файла с аутентификационными данными
if os.path.isfile(utils.dirs.ABS_PATH + '/auth.json'):
    
    with open(utils.dirs.ABS_PATH + '/auth.json') as f:
        auth_data = json.load(f)

    API_ID = auth_data['api_id']
    API_HASH = auth_data['api_hash']
    PHONE_NUMBER = auth_data['phone_number']

else:

    API_ID = input('Enter api id: ')
    API_HASH = input('Enter api hash: ')
    PHONE_NUMBER = input('Enter your phone number: ')

    f = open(utils.dirs.ABS_PATH + '/auth.json', 'w')
    data = json.dumps({
        'auth_date': int(time.time()),
        'api_id': API_ID,
        'api_hash': API_HASH,
        'phone_number': PHONE_NUMBER
    })
    f.write(data)
    f.close()