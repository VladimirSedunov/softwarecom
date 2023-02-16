import json
from json import JSONDecoder

import requests
from requests import Response


def test_get_users_has_avatar_field():
    url = "https://softwarecom.ru/ajax/btnorder.php"

    data = {
        "fio": "sssssssssssssss",
        "phone": "л",
        "email": "vladimir.sedunov@softwarecom.ru",
        "text": "ццц",
        "agree": "Y",
        "ajax": 1
    }
    data = json.dumps(data)

    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Referer': 'https://softwarecom.ru/about/',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'Host': 'softwarecom.ru',
               'Origin': 'https://softwarecom.ru'
               }

    response: Response = requests.post(url=url, data=data, headers=headers)

    print(f'response.status_code={response.status_code}')
    print(response.json())


# def test_001():
#     x = '%u0421%u043A%u0430%u043D%u0435%u0440 %u043F%u0440%u0438'
#     # print(x)
#     # y = x.replace('%', '\\').decode('unicode-escape')
#     y = x.replace('%', '\\')
#     print(y)
#     # dec = JSONDecoder()
#     # z = dec.decode(y)
#     # print(z)
#
#     obj = json.loads(y, cls=json.JSONDecoder)
