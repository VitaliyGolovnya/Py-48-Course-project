import requests
import re
from pprint import pprint

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version    
        }
    
    def get_user_id(self, user_link):
        screen_name = re.split('\/', user_link)[-1]
        url = self.url + 'utils.resolveScreenName'
        params = {'screen_name' : screen_name}
        response = requests.get(url=url, params={**params, **self.params}).json()
        return response['response']['object_id']
    
    def user_name(self, user_link):
        url = self.url +'users.get'
        params = {'users_id' : self.get_user_id(user_link)}
        response = requests.get(url=url, params={**params, **self.params}).json()
        name = response['response'][0]['first_name'] + " " + response['response'][0]['last_name']
        return name


    def get_photos(self, user_link):
        url = self.url + 'photos.get'
        params = {'owner_id' : self.get_user_id(user_link),
            'album_id' : 'profile',
            'extended' : '1',
            'photo_sizes' : '1'}
        response = requests.get(url=url, params={**params, **self.params}).json()
        return response

