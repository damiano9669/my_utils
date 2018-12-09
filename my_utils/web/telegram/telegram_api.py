import os
import urllib

import my_utils.web.json_utils as ju
import shutil
import requests


class telegram_api(object):

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

    def get_last_update(self, updates):
        """
        :param updates:
        :return: last update
        """
        return updates['result'][-1]

    def is_new_update(self, updates):
        """
            check if there is
            a new update
        :param updates:
        :return:
        """
        if len(updates['result']) == 0:
            return False
        result = self.get_last_update(updates)
        update_id = result['update_id']

        if update_id != self.last_update_id:
            self.last_update_id = update_id
            return True
        else:
            return False

    def get_id_name_content_date(self, updates, content_type):
        """
            get info from update
        :param updates:
        :param content_type: text, photo, ecc
        :return:
        """
        result = self.get_last_update(updates)
        message = result['message']
        chat = message['chat']
        chat_id = chat['id']
        first_name = chat['first_name']
        content = message[content_type]
        date = message['date']
        return (chat_id, first_name, content, date)

    def send_file(self, chat_id, content_type, path):
        """
        :param chat_id: id of the chat
        :param content_type: 'photo', 'voice', ... view api
        :param path: path of the file
        :return:
        """
        data = {'chat_id': chat_id}
        file = {content_type: (path, open(path, "rb"))}
        url = urllib.parse.urljoin(self.url, 'send{}'.format(content_type.title()))
        response = requests.post(url, data=data, files=file)
        return response

    def send_message(self, chat_id, text):
        """
            send a message to specific user
        :param chat_id: id of the chat
        :param text: message to send
        :return:
        """
        data = {'chat_id': chat_id,
                'text': text}
        url = urllib.parse.urljoin(self.url, 'sendMessage')
        response = requests.post(url, data=data)
        return response

    def download_file(self, file_id, path, name=None):
        """
            download files
            more general function
        :param file_id: id of file
        :param path: dir to save file
        :param name: name of the file with extension
        :return: file path
        """
        url = urllib.parse.urljoin(self.url, 'getFile?file_id={}'.format(file_id))
        js = ju.get_json(url)
        path_file = js['result']['file_path']
        url = self.telegram_url + 'file' + self.bot_url
        url = urllib.parse.urljoin(url, path_file)
        response = requests.get(url, stream=True)

        path_file = path_file.split('/')[-1]

        # rename file
        if name != None:
            path_file = name

        path_file = os.path.join(path, path_file)

        with open(path_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return path_file

    def get_type_of_response(self, updates):
        """
            check type of update
        :param updates:
        :return:
        """
        result = self.get_last_update(updates)
        message = result['message']

        if 'text' in message:
            return 'text'
        elif 'photo' in message:
            return 'photo'
        elif 'voice' in message:
            return 'voice'
        elif 'document' in message:
            return 'document'
        elif 'audio' in message:
            return 'audio'
        else:
            return None


if __name__ == '__main__':
    pass
