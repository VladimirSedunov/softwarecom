import time

import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene.support.conditions import have
from selene.support.shared import browser


@allure.severity(Severity.NORMAL)
@allure.title('Открыть несуществующую страницу')
@pytest.mark.demo
def test_Открыть_Несуществующую_Страницу():
    with allure.step("Открываем несуществующую страницу"):
        browser.open("/about/err-err-err")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Страница не найдена'))
        assert browser.element('.not-fount-collum-2').should(have.text('Страница которую вы запросили, отсутствует на нашем сайте.'))
        assert browser.element('.not-fount-collum-2 [href="/"]').should(have.exact_text('главной страницей'))

        with allure.step("Делаем скриншот 'Страница_не_найдена'"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="Страница_не_найдена", attachment_type=AttachmentType.JPG)

        browser.element('.not-fount-collum-2 [href="/"]').should(have.exact_text('главной страницей')).click()
        # time.sleep(1)

    with allure.step("Переход на главную страницу"):
        assert browser.element('.page .company_about').element('h1').should(
            have.exact_text('Софт Компани — цифровой системный интегратор.'))
        assert browser.driver.current_url == 'https://softwarecom.ru/'

        with allure.step("Делаем скриншот 'Главная_страница'"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="Главная_страница", attachment_type=AttachmentType.JPG)
