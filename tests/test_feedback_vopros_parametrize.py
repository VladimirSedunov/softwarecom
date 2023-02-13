import time

import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@pytest.mark.parametrize("fio, email, phone, text, is_error, result_message",
                         [
                             ('Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', False,
                              'Спасибо! Ваш запрос принят, в ближайшее время мы с вами обязательно свяжемся.'),

                             ('', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True,
                              'Укажите Ваше Ф.И.О!'),

                             ('Тут Пишем ФИО', '', 'Это_телефон', 'Это сообщение', True,
                              'Укажите правильный e-mail!'),

                             ('Тут Пишем ФИО', 'this_is@email.mail', '', 'Это сообщение', True,
                              'Укажите Ваш контактный телефон!'),

                             ('Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', '', True,
                              'Введите Ваше сообщение!')
                         ])
def test_parametrize(fio, email, phone, text, is_error, result_message):
    with allure.step("Открываем страницу Контакты"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("Открываем диалоговое окно Обратная Связь"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()
        feedback_form = browser.element('#feedbackForm')
        feedback_form.element('[name=fio]').set_value(fio)
        feedback_form.element('[name=email]').set_value(email)
        feedback_form.element('[name=phone]').set_value(phone)
        feedback_form.element('[name=text]').set_value(text)
        time.sleep(1)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()
    if not is_error:
        with allure.step("Успех: запрос принят"):
            s('.msg-wrap').should(have.exact_text(result_message))
    else:
        with allure.step("Сообщение об ошибке: Укажите Ваше Ф.И.О!"):
            feedback_form.element('.js-error').should(have.exact_text(result_message))
    time.sleep(1)