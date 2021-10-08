import requests
import os
from pprint import pprint


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


    def upload_file_to_disk(self, file_path, filename):
        response = self._get_upload_link(file_path=file_path)
        url = response.get("href", "")
        if url:
            response = requests.put(url=url, data=open(filename, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")
        else:
            print('Empty url')


if __name__ == '__main__':
    file_path = 'netology/API/API_task2.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(file_path, 'API_task2.txt')
