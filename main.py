from vk import VkUser
from yandexdisk import YaUploader
import time
import requests
import urllib.request

with open(r'C:\Users\vital\Desktop\Tokens\vk token.txt', 'rt', encoding='utf-8') as f:
    vk = VkUser(f.read().strip())
with open(r'C:\Users\vital\Desktop\Tokens\yandex token.txt', 'rt', encoding='utf-8') as f:
    yandex = YaUploader(f.read().strip())

def backup_copy(user_link):
    photo_dict = vk.get_photos(user_link)
    for photo in photo_dict['response']['items']:
        path_name = 'vk_backup/' + vk.user_name(user_link) + '/Likes: ' + str(photo['likes']['count']) + 'date: ' + time.ctime(photo['date'])
        url = photo['sizes'][-1]['url']
        data = requests.get(url)
        yandex.upload(path_name, data)
    print("Sucess")
    


        
if __name__ == '__main__':
    backup_copy("https://vk.com/rollingonthefloorandlaughing")
