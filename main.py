import requests
import os
from dotenv import load_dotenv
import argparse


def get_bitlink_id(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    value_authorization = 'Bearer {}'.format(token)
    headers = {'Authorization': value_authorization}
    data = {
        'long_url': link,
        'group_guid': 'Bj3hglRLEZl',
        'domain': 'bit.ly'
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    if (response.ok == True):
        return response.json()['id']
    return None


def get_count_clicks(link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)
    value_authorization = 'Bearer {}'.format(token)
    headers = {'Authorization': value_authorization}
    params = {'units': '-1'}
    response = requests.get(url, headers=headers, params=params)

    if (response.ok == True):
        return response.json()['total_clicks']
    return None


def check_link(link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link)
    value_authorization = 'Bearer {}'.format(token)
    headers = {'Authorization': value_authorization}
    response = requests.get(url, headers=headers)

    if (response.ok == True):
        return True
    return False


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("TOKEN")

    parser = argparse.ArgumentParser(description='Скрипт обрезает ссылки с помощью сервиса Битли и возвращает статистику переходов по ним.')
    parser.add_argument('link', help='Введите ссылку')
    args = parser.parse_args()
    link = args.link

    if check_link(link) == True:
        count_clicks = get_count_clicks(link)
        print('number of links =', count_clicks)
    else:
        try:
            short_link = get_bitlink_id(token, link)
            print(short_link)
        except requests.exceptions.HTTPError as error:
            exit('Can,t get data from server:\n{0}'.format(error))
