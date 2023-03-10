import time

import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@pytest.mark.skip
@pytest.mark.parametrize("title, fio, email, phone, text, pers_data_agree, is_error, result_message",
                         [
                             ('Позитивный сценарий','Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, False,
                              '!!! Это намеренный FAIL теста !!!   Спасибо! Ваш запрос принят, в ближайшее время мы с вами обязательно свяжемся.'),

                             ('Нет ФИО', '', 'this_is@email.mail', 'Это_телефон', 'Это сообщение', True, True, 'Укажите Ваше Ф.И.О!'),
                             ('Нет email', 'Тут Пишем ФИО', '', 'Это_телефон', 'Это сообщение', False, True, 'Укажите правильный e-mail!'),
                             ('Нет телефона', 'Тут Пишем ФИО', 'this_is@email.mail', '', 'Это сообщение', True, True, 'Укажите Ваш контактный телефон!'),
                             ('Нет сообщения', 'Тут Пишем ФИО', 'this_is@email.mail', 'Это_телефон', '', False, True, 'Введите Ваше сообщение!')
                         ])
def test_parametrize(title, fio, email, phone, text, pers_data_agree, is_error, result_message):

    allure.dynamic.title(title)

    with allure.step("ТС5.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС5.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС5.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value(fio)
        feedback_form.element('[name=email]').set_value(email)
        feedback_form.element('[name=phone]').set_value(phone)
        feedback_form.element('[name=text]').set_value(text)
        if pers_data_agree != len(feedback_form.all('.agreeDiv.selected').should(be.existing)) > 0:
            feedback_form.element('.agreeDiv').should(be.clickable).click()
        time.sleep(1)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    if not is_error:
        with allure.step(f"ТС5.4. Получить сообщение ({result_message})"):
        # with allure.step(f"Успех: {result_message}"):
            s('.msg-wrap').should(have.exact_text(result_message))
    else:
        with allure.step(f"ТС5.4. Получить сообщение ({result_message})"):
            feedback_form.element('.js-error').should(have.exact_text(result_message))
    time.sleep(1)
