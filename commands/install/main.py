import os, time, requests, zipfile, shutil
import utils.dirs, utils.module_init

def change_url(url):

    url = url.endswith('.git') == True and url[:-4] or url
    new_url = f'{url}/archive/refs/heads/main.zip'

    return new_url

def download_archive(url, module_name):

    repo_name = url.split('/')[4]

    os.mkdir(f'{utils.dirs.ABS_PATH}modules/{module_name}')

    response = requests.get(url)
    
    with open(f'{utils.dirs.ABS_PATH}modules/{module_name}/main.zip', 'wb') as file:
        file.write(response.content)

    with zipfile.ZipFile(f'{utils.dirs.ABS_PATH}modules/{module_name}/main.zip') as zip_ref:
        zip_ref.extractall(f'{utils.dirs.ABS_PATH}modules/{module_name}')

    source_dir = f'{utils.dirs.ABS_PATH}modules/{module_name}/{repo_name}-main'
    target_dir = f'{utils.dirs.ABS_PATH}modules/{module_name}'

    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, filename)
        target_file_path = os.path.join(target_dir, filename)
        shutil.move(source_file_path, target_file_path)
    
    shutil.rmtree(source_dir)
    os.remove(f'{utils.dirs.ABS_PATH}modules/{module_name}/main.zip')

def response(client, message, app):

    text = message.text.split(' ', maxsplit = 4)
    url = change_url(text[1])
    module_name = text[3]

    with open(f'{utils.dirs.COMMANDS_PATH}install/waiting.html', encoding='utf-8') as f:
        message_text = f.read()
        message.edit_text(message_text)

    try:
        with open(f'{utils.dirs.COMMANDS_PATH}install/success.html', encoding='utf-8') as f:
            message_text = f.read()
            message.edit_text(message_text)

        download_archive(url, module_name)
        time.sleep(1)
        utils.module_init.INIT(app, module_name)

    except Exception as e:
        message.edit_text('<b>ㅤ\n' + str(e) + '\nㅤ</b>')