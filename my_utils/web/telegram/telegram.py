import os
import urllib

import my_utils.web.json_utils as ju
import shutil
import requests


class telegram(object):

    def __init__(self, token):
        """
        :param token: bot token, get it from BotFather
        """
        self.token = token

        self.telegram_url = 'https://api.telegram.org/'
        self.bot_url = '/bot{}/'.format(token)

        self.url = urllib.parse.urljoin(self.telegram_url, self.bot_url)

        self.last_update_id = None  # to check if is new message

    def get_updates(self):
        """
            get update from telegram
        :return:
        """
        url = urllib.parse.urljoin(self.url, 'getUpdates')
        js = ju.get_json(url)
        return js

    def is_new_update(self, updates):
        """
            check if there is
            a new update
        :param updates:
        :return:
        """
        if len(updates['result']) == 0:
            return False
        result = updates['result'][-1]
        update_id = result['update_id']

        if update_id != self.last_update_id:
            self.last_update_id = update_id
            return True
        else:
            return False

    def get_id_name_content_date(self, updates, content_type='text'):
        """
            get info from update
        :param updates:
        :param content_type: text, photo, ecc
        :return:
        """
        result = updates['result'][-1]
        message = result['message']
        chat = message['chat']
        user_id = chat['id']
        first_name = chat['first_name']
        content = message[content_type]
        date = message['date']
        return (user_id, first_name, content, date)

    def send_message(self, user_id, message):
        """
            send a message to specific user
        :param user_id:
        :param message:
        :return:
        """
        url = urllib.parse.urljoin(self.url, 'sendMessage?text={}&chat_id={}'.format(message, user_id))
        return ju.get_response(url)

    def download_file(self, file_id, path):
        """
            download files
            more general function
        :param file_id: id of file
        :param path: dir to save file
        :return:
        """
        url = urllib.parse.urljoin(self.url, 'getFile?file_id={}'.format(file_id))
        js = ju.get_json(url)
        path_file = js['result']['file_path']
        url = self.telegram_url + 'file' + self.bot_url
        url = urllib.parse.urljoin(url, path_file)
        response = requests.get(url, stream=True)

        path_file = path_file.split('/')[-1]

        with open(os.path.join(path, path_file), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return path_file

    def download_photo(self, updates, path, quality=2):
        """
            download photo from user
        :param path: directory path to save image
        :param quality: 1 (bad quality), 2 (medium quality), 3 (best quality)
        :return: tuple (user_id, name, path_image, date)
        """
        user_id, name, photos, date = self.get_id_name_content_date(updates, content_type='photo')
        file_id = photos[quality]['file_id']

        path_image = self.download_file(file_id, path)

        return (user_id, name, path_image, date)

    def download_voice_message(self, updates, path):
        """
            download voice message from user
        :param path: directory path to save voice message
        :return: tuple (user_id, name, path_message, date)
        """
        user_id, name, voice, date = self.get_id_name_content_date(updates, content_type='voice')
        file_id = voice['file_id']

        path_voice = self.download_file(file_id, path)

        return (user_id, name, path_voice, date)

    def upload_photo(self, user_id, path):
        """
            send image to specific user id
        :param user_id:
        :param path: image path to send
        :return:
        """
        data = {'chat_id': user_id}
        files = {'photo': (path, open(path, "rb"))}
        url = urllib.parse.urljoin(self.url, 'sendPhoto')
        requests.post(url, data=data, files=files)
        return True

    def upload_voice_message(self, user_id, path):
        """
            send voice message to specific user id
        :param user_id:
        :param path: voice path to send
        :return:
        """
        data = {'chat_id': user_id}
        files = {'voice': (path, open(path, "rb"))}
        url = urllib.parse.urljoin(self.url, 'sendVoice')
        requests.post(url, data=data, files=files)
        return True

    def get_type_of_response(self, updates):
        """
            check type of update
        :param updates:
        :return:
        """
        result = updates['result'][-1]
        message = result['message']

        if 'text' in message:
            return 'text'
        elif 'photo' in message:
            return 'photo'
        elif 'voice' in message:
            return 'voice'
        else:
            return None


if __name__ == '__main__':
    token = '...'
    bot = telegram(token)

    download_dir_path = '...'

    while True:
        updates = bot.get_updates()
        if bot.is_new_update(updates):
            print('New update')
            content = bot.get_type_of_response(updates)
            print('content', content)
            if content == 'text':
                print('text')
                id, name, message, date = bot.get_id_name_content_date(updates)
                message = 'Hi {}, this is your id: {}\nThis is your message:{}'.format(name, id, message)
                bot.send_message(id, message)
            elif content == 'photo':
                print('photo')
                id, name, image, date = bot.download_photo(updates, download_dir_path)
                bot.upload_photo(id, os.path.join(download_dir_path, image))
            elif content == 'voice':
                id, name, voice, date = bot.download_voice_message(updates, download_dir_path)
                bot.upload_voice_message(id, os.path.join(download_dir_path, voice))
