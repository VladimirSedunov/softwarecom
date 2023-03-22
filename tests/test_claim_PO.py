import os
import time
import allure
import pytest

from tests.test_claim_dir.data.claim_data import Claim
from tests.test_claim_dir.model.pages.form_claim import Form_Claim
from tests.test_claim_dir.model.pages.form_main import Form_Main


SLEEP_TIME = 1.0

list_claim = [
    Claim('Позитивный сценарий', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, False, 'Ваш запрос отправлен менеджеру!'),
    Claim('Нет ФИО', '', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, True, 'Укажите Ваше Ф.И.О!'),
    Claim('Нет телефона', 'Тут Пишем ФИО', 'this_is@email.mail', '', 'Это сообщение', False, True, 'Укажите Ваш контактный телефон!'),
    Claim('Нет email', 'Тут Пишем ФИО', '', 'Это_телефон', 'Это сообщение', True, True, 'Укажите правильный e-mail!'),
    Claim('Нет сообщения', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', '', False, True, 'Введите Ваше сообщение!'),
]


@allure.title('ТС6. Отправка заявки с главной страницы (с использованием Page Object). ')
@pytest.mark.jenkins_ok
@pytest.mark.current_debug
# @pytest.mark.skip
# @pytest.mark.xfail('err')
@pytest.mark.parametrize("claim", list_claim)
def test_claim_form(setup_browser, claim):

    browser = setup_browser
    base_url = os.getenv('BASE_URL')

    allure.dynamic.title('ТС6. Отправка заявки с главной страницы (с использованием Page Object). ' + claim.title)

    form_main = Form_Main(base_url)

    with allure.step("ТС6.1. Открыть страницу 'Компания'"):
        form_main.open(browser)
        form_main.check(browser)

    with allure.step("ТС6.2. Открыть диалоговое окно 'Сделать запрос'"):
        form_main.open_claim_form(browser)

    with allure.step("ТС6.3. Заполнить реквизиты формы"):
        form_claim = Form_Claim()
        form_claim.fill(claim, browser)
        form_claim.submit(browser)

    with allure.step(f"ТС6.4. Получить сообщение ({claim.expected_result_message})"):
        form_claim.check(claim, browser)

    time.sleep(SLEEP_TIME)
