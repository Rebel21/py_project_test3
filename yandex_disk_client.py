import os

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = 'https://cloud-api.yandex.net:443'
        self.publish = '/v1/disk/resources/publish'
        self.uploaded_files = '/v1/disk/resources/public'
        self.upload_file = '/v1/disk/resources/upload'

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        headers = {'Authorization': f'OAuth {self.token}'}
        r = requests.get(url=f'{self.host}{self.upload_file}?path={file_path}', headers=headers, timeout=10)
        response = requests.put(url=r.json()['href'], headers=headers, timeout=10)
        if response.status_code == 201:
            return f'Файл {file_path} успешно загружен'



    def get_uploaded_files(self):
        headers = {'Authorization': f'OAuth {self.token}'}
        res = requests.get(f'{self.host}{self.uploaded_files}', headers=headers, timeout=10)
        return res.json()


if __name__ == '__main__':
    uploader = YaUploader('API_KEY')
    print(uploader.upload('file_for_upload.txt'))
