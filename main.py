from vk import VkUser
from yandexdisk import YaUploader
from datetime import datetime


def backup_copy(user_link, vktoken, yandextoken):
    vk = VkUser(vktoken)
    yandex = YaUploader(yandextoken)
    yandex.create_folder('disk:/vk_backup')
    photo_dict = vk.get_photos(user_link)
    for photo in photo_dict['response']['items']:
        yandex.create_folder('disk:/vk_backup/' + vk.get_user(user_link)[1])
        file_path = f"disk:/vk_backup/{vk.get_user(user_link)[1]}/{str(photo['likes']['count'])} likes date: {datetime.utcfromtimestamp(photo['date']).strftime('%Y-%m-%d')}.jpg"
        url = photo['sizes'][-1]['url']
        yandex.upload_from_url(file_path, url)
    
with open(r'C:\Users\vital\Desktop\Tokens\vk token.txt', 'rt', encoding='utf-8') as f:
    vktoken = f.read().strip()
with open(r'C:\Users\vital\Desktop\Tokens\yandex token.txt', 'rt', encoding='utf-8') as f:
    yandexktoken = f.read().strip()

        
if __name__ == '__main__':

    backup_copy("https://vk.com/id218525920", vktoken=vktoken, yandextoken=yandexktoken)
