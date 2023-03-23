import os
import time
import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene.support.conditions import have, be
from selene.core.entity import Browser

SLEEP_TIME = 5.0
SLEEP_TIME2 = 1.0


@allure.title('ТС4. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" : Сообщение (запрос принят)')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_positive(setup_browser):

    # pytest.fail('!!! ERROR !!! ')

    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС4.1. Открыть страницу 'Контакты'"):
        # browser.open(f"{base_url}/contacts/")
        browser.open(f"/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС4.3. Заполнить реквизиты формы"):
        browser.element('#feedbackForm').with_(timeout=SLEEP_TIME)
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4.4. Получить сообщение (запрос принят)"):
        browser.element('.msg-wrap').with_(timeout=SLEEP_TIME).should(have.exact_text('Спасибо! Ваш запрос принят, в ближайшее время мы с вами обязательно свяжемся.'))
        allure.attach(browser.driver.get_screenshot_as_png(), name="Сообщение (запрос принят)", attachment_type=AttachmentType.JPG)


@allure.title('ТС4. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" : Сообщение об ошибке: Укажите Ваше Ф.И.О!')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_blank_fio(setup_browser):
    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС4а.1. Открыть страницу 'Контакты'"):
        # browser.open(f"{base_url}/contacts/")
        browser.open(f"/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4а.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС4а.3. Заполнить реквизиты формы"):
        browser.element('#feedbackForm').with_(timeout=SLEEP_TIME)
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4а.4. Получить сообщение об ошибке: Укажите Ваше Ф.И.О!"):
        feedback_form.element('.js-error').with_(timeout=SLEEP_TIME).should(have.exact_text('Укажите Ваше Ф.И.О!'))
        allure.attach(browser.driver.get_screenshot_as_png(), name="Сообщение об ошибке: Укажите Ваше Ф.И.О!", attachment_type=AttachmentType.JPG)


@allure.title('ТС4. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" : Сообщение об ошибке: Укажите правильный e-mail!')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_blank_email(setup_browser):
    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС4б.1. Открыть страницу 'Контакты'"):
        # browser.open(f"{base_url}/contacts/")
        browser.open(f"/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4б.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС4б.3. Заполнить реквизиты формы"):
        browser.element('#feedbackForm').with_(timeout=SLEEP_TIME)
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Укажите правильный e-mail!"):
        feedback_form.element('.js-error').with_(timeout=SLEEP_TIME).should(have.exact_text('Укажите правильный e-mail!'))
        allure.attach(browser.driver.get_screenshot_as_png(), name="Сообщение об ошибке: Укажите правильный e-mail!", attachment_type=AttachmentType.JPG)


@allure.title('ТС4. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" : Сообщение об ошибке: Укажите Ваш контактный телефон!')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_blank_phone(setup_browser):
    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС4в.1. Открыть страницу 'Контакты'"):
        # browser.open(f"{base_url}/contacts/")
        browser.open(f"/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4в.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС4в.3. Заполнить реквизиты формы"):
        browser.element('#feedbackForm').with_(timeout=SLEEP_TIME)
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('')
        feedback_form.element('[name=text]').set_value('Это сообщение')
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Укажите Ваш контактный телефон!"):
        feedback_form.element('.js-error').with_(timeout=SLEEP_TIME).should(have.exact_text('Укажите Ваш контактный телефон!'))
        allure.attach(browser.driver.get_screenshot_as_png(), name="Сообщение об ошибке: Укажите Ваш контактный телефон!", attachment_type=AttachmentType.JPG)


@allure.title('ТС4. Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" : Сообщение об ошибке: Введите Ваше сообщение!')
@allure.severity(Severity.NORMAL)
@pytest.mark.jenkins_ok
# @pytest.mark.skip
def test_blank_text(setup_browser):
    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС4г.1. Открыть страницу 'Контакты'"):
        # browser.open(f"{base_url}/contacts/")
        browser.open(f"/contacts/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС4г.2. Открыть диалоговое окно Обратная Связь / Задать вопрос"):
        browser.element('.callback-panel-btn').with_(timeout=SLEEP_TIME).click()
        browser.element('.c-ico-chat').with_(timeout=SLEEP_TIME).should(be.clickable).click()

    with allure.step("ТС4г.3. Заполнить реквизиты формы"):
        browser.element('#feedbackForm').with_(timeout=SLEEP_TIME)
        feedback_form = browser.element('#feedbackForm')
        assert browser.element('#feedbackForm').with_(timeout=SLEEP_TIME).element('.h1').with_(timeout=SLEEP_TIME).should(have.exact_text('Обратная связь'.upper()))

        feedback_form.element('[name=fio]').set_value('Тут Пишем ФИО')
        feedback_form.element('[name=email]').set_value('this_is@email.mail')
        feedback_form.element('[name=phone]').set_value('Это_телефон')
        feedback_form.element('[name=text]').set_value('')
        time.sleep(SLEEP_TIME2)
        feedback_form.element('[type=submit][name=send]').should(be.clickable).click()

    with allure.step("ТС4б.4. Получить сообщение об ошибке: Введите Ваше сообщение!"):
        feedback_form.element('.js-error').with_(timeout=SLEEP_TIME).should(have.exact_text('Введите Ваше сообщение!'))
        allure.attach(browser.driver.get_screenshot_as_png(), name="Сообщение об ошибке: Введите Ваше сообщение!", attachment_type=AttachmentType.JPG)
