# https://softwarecom.ru/about/   -   О компании   -   Отправить заявку   -   Сделать запрос
import os
# from time import sleep

import allure
import pytest
import requests
from requests import Response
from dataclasses import dataclass
from selene.support.conditions import be
from selene.support.shared import browser


@dataclass
class Claim_about:
    fio: str
    phone: str
    email: str
    text: str
    agree: str
    ajax: int
    is_error: bool
    status_code: int
    status: str
    expected_message: str

    def __init__(self, title, fio, phone, email, text, agree, ajax, is_error, status_code, status, expected_message):
        self.title = title
        self.fio = fio
        self.phone = phone
        self.email = email
        self.text = text
        self.agree = agree
        self.ajax = ajax
        self.is_error = is_error
        self.status_code = status_code
        self.status = status
        self.expected_message = expected_message


list_claim_about = [
    Claim_about('Позитивный сценарий', 'Тут Пишем ФИО', 'Это_телефон', 'this_is@email.mail', 'Это сообщение', "Y", 1,
                False, 200, 'success', 'Ваш запрос отправлен менеджеру!'),
    Claim_about('Нет ФИО', '', 'Это_телефон', 'this_is@email.mail', 'Это сообщение', "Y", 1,
                True, 200, 'error', 'Укажите Ваше Ф.И.О!'),
    Claim_about('Нет телефона', 'Тут Пишем ФИО', '', 'this_is@email.mail', 'Это сообщение', "Y", 1,
                True, 200, 'error', 'Укажите Ваш контактный телефон!'),
    Claim_about('Нет email', 'Тут Пишем ФИО', 'Это_телефон', '', 'Это сообщение', "Y", 1,
                True, 200, 'error', 'Укажите правильный e-mail!'),
    Claim_about('Нет сообщения', 'Тут Пишем ФИО', 'Это_телефон', 'this_is@email.mail', '', "Y", 1,
                True, 200, 'error', 'Введите Ваше сообщение!')
]


@pytest.mark.parametrize("claim_about", list_claim_about)
def test_API_Отправить_Заявку(claim_about):
    url = "https://softwarecom.ru/ajax/btnorder.php"
    is_robot = True
    mess_is_robot = 'Your are robot!'
    # sleep(1.1)

    with allure.step("ТС8.1. Сформировать POST-запрос"):

        while is_robot:
            is_robot = False
            cookie = cookies_read_from_file()

            data = {"fio": f"{claim_about.fio}",
                    "phone": f"{claim_about.phone}",
                    "email": f"{claim_about.email}",
                    "text": f"{claim_about.text}",
                    "agree": f"{claim_about.agree}",
                    "ajax": f"{claim_about.ajax}",
                    "is_error": f"{claim_about.is_error}",
                    "status_code": f"{claim_about.status_code}",
                    "status": f"{claim_about.status}",
                    "expected_message": f"{claim_about.expected_message}"
                    }

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'softwarecom.ru',
                'Origin': 'https://softwarecom.ru',
                'Referer': 'https://softwarecom.ru/about/',
                'Cookie': f'{cookie};'
            }

            with allure.step("ТС8.2. Получить ответ"):
                response: Response = requests.post(url=url, data=data, headers=headers)
                real_status_code = response.status_code
                real_is_err = response.json()[0]
                real_message = response.json()[1]
                print()
                print(response.json())

                if real_message == mess_is_robot:
                    cookie = cookies_get_from_UI()
                    cookies_write_to_file(cookie)
                    is_robot = True

    with allure.step("ТС8.2. Проверить корректность ответа"):
        assert real_status_code == claim_about.status_code
        assert real_is_err == claim_about.status
        assert real_message == claim_about.expected_message


def cookies_get_from_UI():
    print('cookies_get_from_UI')
    browser.open("/about/")
    browser.driver.minimize_window()
    browser.element('.order-btn-popup').click()

    order_form = browser.element('#orderForm')
    order_form.element('[name=fio]').set_value('Тут Пишем ФИО')
    order_form.element('[name=phone]').set_value('7 903 937 33 33')
    order_form.element('[name=email]').set_value('this_is@email.mail')
    order_form.element('[name=text]').set_value('Это сообщение')
    order_form.element('[type=submit][name=send]').should(be.clickable).click()

    # Return The List of all Cookies
    cookie = ''
    result = browser.driver.get_cookies()
    for s in result:
        name = s.get('name')
        if len(name) == 32:
            value = s.get('value')
            cookie = f'{name}={value}'
    return cookie


def cookies_read_from_file():
    # годится для Linux и для Windows одновременно
    dir_down = str(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources')))
    fname = os.path.join(dir_down, "test_api_cookies.txt")
    with open(fname, 'r') as f:
        q = f.read()
    return q


def cookies_write_to_file(cookie):
    # годится для Linux и для Windows одновременно
    dir_down = str(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources')))
    fname = os.path.join(dir_down, "test_api_cookies.txt")
    with open(fname, 'w') as f:
        f.write(cookie)
