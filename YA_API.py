import requests


def create_folder():
    name_folder = input('Введите название папки: ')
    token = ''
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'authorization': f'OAuth {token}'
    }

    response = requests.put(url, params={'path': {name_folder}}, headers=headers)
    return str(response)
def delete_folder():
    name_folder = input('Введите название папки: ')
    token = ''
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'authorization': f'OAuth {token}'
    }

    response = requests.delete(url, params={'path': {name_folder}}, headers=headers)
    return str(response)

# print(create_folder())
# print(delete_folder())
