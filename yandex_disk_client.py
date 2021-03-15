import os

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = 'https://cloud-api.yandex.net:443'
        self.publish = '/v1/disk/resources/publish'
        self.uploaded_files = '/v1/disk/resources/public'

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        headers = {'Authorization': f'OAuth {self.token}'}
        #res = requests.post()
        response = requests.put(url=f'{self.host}{self.publish}'
                                    f'?path={os.path.abspath(file_path)}', headers=headers, timeout=10)
        return response.json(), response.url

    def get_uploaded_files(self):
        headers = {'Authorization': f'OAuth {self.token}'}
        res = requests.get(f'{self.host}{self.uploaded_files}', headers=headers, timeout=10)
        return res.json()


if __name__ == '__main__':
    uploader = YaUploader('AgAAAAABYL-IAADLW_VMyX7tLUOjpyDLoHp2vpI')
    print(uploader.upload('test.txt'))
    #print(uploader.get_uploaded_files())
