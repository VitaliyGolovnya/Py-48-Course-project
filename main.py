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
    yandex.create_folder('/vk_backup')
    photo_dict = vk.get_photos(user_link)
    for photo in photo_dict['response']['items']:
        yandex.create_folder('/vk_backup/' + vk.user_name(user_link))
        file_path = 'vk_backup/' + vk.user_name(user_link) + '/Likes: ' + str(photo['likes']['count']) + ' date: ' + time.ctime(photo['date']) + '.png'
        url = photo['sizes'][-1]['url']
        yandex.upload_from_url(file_path, url)
    


        
if __name__ == '__main__':
    backup_copy("https://vk.com/rollingonthefloorandlaughing")
