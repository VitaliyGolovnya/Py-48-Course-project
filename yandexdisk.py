import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            "Content-Type" : "application/json",
            "Authorization" : f"OAuth {self.token}"
        }
    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path" : file_path, "overwrite" : "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, data):
        href_dict = self._get_upload_link(file_path=file_path)
        href = href_dict.get("href")
        response = requests.put(href, data)
        response.raise_for_status()
    
    def upload_from_url(self, file_path, url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            'url' : url,
            'path' : file_path
            }
        response = requests.post(url=upload_url, headers=headers, params=params)
        # if response.status_code == 202:
        #     print('Image uploaded')
    
    def create_folder(self, folder_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path' : folder_path}
        response = requests.put(url=url, headers=self.get_headers(), params=params)
        if response.status_code == 201:
            print(f"Folder {folder_path} created")        
        



