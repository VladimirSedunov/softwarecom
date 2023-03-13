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
def test_positive():
    with allure.step("ТС4.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС4.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4.4. Получить сообщение (запрос принят)"):
        s('.msg-wrap').should(have.exact_text('Спасибо! Ваш запрос принят, в ближайшее время мы с вами обязательно свяжемся.'))


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@pytest.mark.skip
def test_blank_fio():
    with allure.step("ТС4а.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4а.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС4а.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        # pers_data_agree = feedback_form.element('.agreeDiv').should(be.clickable).click()
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4а.4. Получить сообщение об ошибке: Укажите Ваше Ф.И.О!"):
        feedback_form.element('.js-error').should(have.exact_text('Укажите Ваше Ф.И.О!'))


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@pytest.mark.skip
def test_blank_email():
    with allure.step("ТС4б.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4б.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС4б.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(1)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()
        time.sleep(2)

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Укажите правильный e-mail!"):
        feedback_form.element('.js-error').should(have.exact_text('Укажите правильный e-mail!'))


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
@pytest.mark.skip
def test_blank_phone():
    with allure.step("ТС4в.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4в.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС4в.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(1)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()
        time.sleep(2)

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Укажите Ваш контактный телефон!"):
        feedback_form.element('.js-error').should(have.exact_text('Укажите Ваш контактный телефон!'))


@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_blank_text():
    with allure.step("ТС4г.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4г.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        s('.callback-panel-btn').click()
        s('.c-ico-chat').click()

    with allure.step("ТС4г.3. Заполнить реквизиты формы"):
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').element('.h1').should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('')
        time.sleep(1)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()
        time.sleep(2)

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Введите Ваше сообщение!"):
        feedback_form.element('.js-error').should(have.exact_text('Введите Ваше сообщение!'))
