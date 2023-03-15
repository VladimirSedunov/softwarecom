import os
import time
import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have, be

SLEEP_TIME = 9.0
SLEEP_TIME2 = 2.0

testdata = [
    ('Позитивный сценарий', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, False,
     'Спасибо! Ваш запрос принят, в ближайшее время мы с вами обязательно свяжемся.'),
    ('Нет ФИО', '', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, True, 'Укажите Ваше Ф.И.О!'),
    ('Нет email', 'Тут Пишем ФИО', '', 'Это_телефон', 'Это сообщение', False, True, 'Укажите правильный e-mail!'),
    ('Нет телефона', 'Тут Пишем ФИО', 'this_is@email.mail', '', 'Это сообщение', True, True, 'Укажите Ваш контактный телефон!'),
    ('Нет сообщения', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', '', False, True, 'Введите Ваше сообщение!')
]


@allure.title('ТС5. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" (Параметризованный тест)')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
@pytest.mark.parametrize("title, fio, email, phone, text, pers_data_agree, is_error, result_message", testdata)
def test_parametrize(setup_browser, title, fio, email, phone, text, pers_data_agree, is_error, result_message):
    browser = setup_browser
    base_url = os.getenv('BASE_URL')

    allure.dynamic.title('ТС5. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" (Параметризованный тест). ' + title)

    with allure.step("ТС5.1. Открыть страницу 'Контакты'"):
        browser.open(f"{base_url}/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС5.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС5.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value(fio)
        feedback_form.element('[name=email]').set_value(email)
        feedback_form.element('[name=phone]').set_value(phone)
        feedback_form.element('[name=text]').set_value(text)
        if pers_data_agree != len(feedback_form.all('.agreeDiv.selected').should(be.existing)) > 0:
            feedback_form.element('.agreeDiv').should(be.clickable).click()
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    if not is_error:
        with allure.step(f"ТС5.4. Получить сообщение ({result_message})"):
            browser.element('.msg-wrap').with_(timeout=SLEEP_TIME).should(have.exact_text(result_message))
    else:
        with allure.step(f"ТС5.4. Получить сообщение ({result_message})"):
            feedback_form.element('.js-error').with_(timeout=SLEEP_TIME).should(have.exact_text(result_message))
    time.sleep(SLEEP_TIME2)
