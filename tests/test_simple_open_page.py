import datetime
import time

import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene.support.conditions import have
from selene.support.shared import browser


@allure.severity(Severity.NORMAL)
@allure.title('ТС1. Открыть несуществующую страницу')
@pytest.mark.demo
def test_Проверка_Основной_Страницы():
    browser.open("/")
    with allure.step("ТС1.1. Открыть главную страницу"):
        assert browser.element('.page .company_about').element('h1').should(
            have.exact_text('Софт Компани — цифровой системный интегратор.'))
        assert browser.driver.current_url == 'https://softwarecom.ru/'

        with allure.step("ТС1.2. Сделать скриншот главной страницы'"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="Главная_страница", attachment_type=AttachmentType.JPG)

    with allure.step("ТС1.3. Проверить копирайт в нижней части страницы"):
        text_copyright = browser.element('.page-footer_text .foot-coll-1').locate().text
        assert text_copyright.startswith('Софт Компани — цифровой интегратор © ')
        assert text_copyright.endswith(str(datetime.date.today().year))

    with allure.step("ТС1.4. Открыть несуществующую страницу"):
        browser.open("/about/err-err-err")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Страница не найдена'))
        assert browser.element('.not-fount-collum-2').should(have.text('Страница которую вы запросили, отсутствует на нашем сайте.'))
        assert browser.element('.not-fount-collum-2 [href="/"]').should(have.exact_text('главной страницей'))

        with allure.step("ТС1.5. Сделать скриншот появившейся страницы"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="Страница_не_найдена", attachment_type=AttachmentType.JPG)
