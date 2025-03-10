import os, requests, zipfile, shutil


def clone(url, path):
    repo_name = url.split('/')[4]

    os.mkdir(path)

    response = requests.get(url)
    
    with open(path + '/main.zip', 'wb') as file:
        file.write(response.content)

    with zipfile.ZipFile(path + '/main.zip') as zip_ref:
        zip_ref.extractall(path)

    source_dir = path + '/' + repo_name + '-main'
    target_dir = path

    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, filename)
        target_file_path = os.path.join(target_dir, filename)
        shutil.move(source_file_path, target_file_path)
    
    shutil.rmtree(source_dir)
    os.remove(path + '/main.zip')