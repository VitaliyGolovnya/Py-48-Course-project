from vk import VkUser
from yandexdisk import YaUploader
from datetime import datetime
from progress.bar import Bar
import json

def backup_copy(user_link, vktoken, yandextoken):
    vk = VkUser(vktoken)
    yandex = YaUploader(yandextoken)
    yandex.create_folder('disk:/vk_backup')
    photo_dict = vk.get_photos(user_link)
    yandex.create_folder('disk:/vk_backup/' + vk.get_user(user_link)[1])
    photos = []
    with Bar('Loading...', max=len(photo_dict['response']['items'])) as bar:
        for photo in photo_dict['response']['items']:
            file_path = f"disk:/vk_backup/{vk.get_user(user_link)[1]}/{str(photo['likes']['count'])} likes date: {datetime.utcfromtimestamp(photo['date']).strftime('%Y-%m-%d')}.jpg"
            url = photo['sizes'][-1]['url']
            yandex.upload_from_url(file_path, url)
            photos += [{
                "file_name" : f"{str(photo['likes']['count'])} likes date: {datetime.utcfromtimestamp(photo['date']).strftime('%Y-%m-%d')}.jpg",
                "size" : photo['sizes'][-1]['type']
            }]
            bar.next()
    json_file = json.dumps(photos)
    with open(f"{vk.get_user(user_link)[1]}.json", "wt", encoding="cp1251") as file:
        file.write(json_file)
    print("Back up completed")

with open(r'C:\Users\vital\Desktop\Tokens\vk token.txt', 'rt', encoding='utf-8') as f:
    vktoken = f.read().strip()

        
if __name__ == '__main__':

    backup_copy(user_link=input('Enter a VK user link: '), vktoken=vktoken, yandextoken=input("Enter unique Yandex Disk token: "))
