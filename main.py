from vk import VkUser
from yandexdisk import YaUploader

with open('C:\Users\vital\Desktop\Tokens\vk token.txt', 'rt') as f:
    vk = VkUser(f.read().strip())
with open('C:\Users\vital\Desktop\Tokens\yandex token.txt', 'rt') as f:
    yandex = YaUploader(f.read().strip())

def backup_copy(user_link):
    photo_dict = vk.get_photos(user_link)
    for photo in photo_dict['response']['items']:
        yandex.upload('vk_backup/' + photo['likes']['count'])
    


        
if __name__ == '__main__':
