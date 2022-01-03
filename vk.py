import requests
import re

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version    
        }
    
    def get_user(self, user_link):
        screen_name = re.split('\/', user_link)[-1]
        url = self.url +'users.get'
        params = {'user_ids' : screen_name}
        response = requests.get(url=url, params={**params, **self.params}).json()
        name = response['response'][0]['first_name'] + " " + response['response'][0]['last_name']
        id = response['response'][0]['id']
        return [id, name]

    def get_photos(self, user_link):
        url = self.url + 'photos.get'
        params = {'owner_id' : self.get_user(user_link)[0],
            'album_id' : 'profile',
            'extended' : '1',
            'photo_sizes' : '1'}
        response = requests.get(url=url, params={**params, **self.params}).json()
        return response