import json
import requests


def get_response(url):
    """
        get response from server
    :param url: url
    :return:
    """
    response = requests.post(url)
    content = response.content.decode('utf8')
    return content


def get_json(url):
    """
        get json from server
    :param url: url
    :return:
    """
    content = get_response(url)
    js = json.loads(content)
    return js
