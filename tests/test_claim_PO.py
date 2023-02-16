import time

import allure
import pytest

from tests.test_claim_dir.model.pages.form_claim import Claim, Form_Claim
from tests.test_claim_dir.model.pages.form_main import Form_Main

list_claim = [
    Claim('Позитивный сценарий', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, False, 'Ваш запрос отправлен менеджеру!'),
    Claim('Нет ФИО', '', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, True, 'Укажите Ваше Ф.И.О!'),
    Claim('Нет телефона', 'Тут Пишем ФИО', 'this_is@email.mail', '', 'Это сообщение', False, True, 'Укажите Ваш контактный телефон!'),
    Claim('Нет email', 'Тут Пишем ФИО', '', 'Это_телефон', 'Это сообщение', True, True, 'Укажите правильный e-mail!'),
    Claim('Нет сообщения', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', '', False, True, 'Введите Ваше сообщение!')
]


@pytest.mark.parametrize("claim", list_claim)
def test_claim_form(claim):
    allure.dynamic.title(claim.title)

    form_main = Form_Main()
    form_main.open()
    form_main.check()
    form_main.open_claim_form()

    form_claim = Form_Claim()
    form_claim.fill(claim)
    form_claim.submit()

    form_claim.check(claim)
    with allure.step(f"Сообщение об ошибке: {claim.expected_result_message}"):
        pass
    time.sleep(2)
