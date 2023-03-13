import json
import os
import time
import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene import command, be, have
from selene.core.entity import Browser
from allure import attachment_type

SLEEP_TIME = 0.5
SLEEP_TIME2 = 1


@allure.severity(Severity.CRITICAL)
@allure.title('ТС2. Проверка работоспособности пунктов и подпунктов главного меню')
# @pytest.mark.skip
@pytest.mark.jenkins_ok
def test_show_main_menu_and_all_submenu(setup_browser):
    def go_throw_main_menu():
        first_level_menu = browser.all('.js-first-level')
        list_ = []
        for item in first_level_menu:
            list_.append(item.locate().text)
        assert len(first_level_menu) == 6
        assert (list_ == ['О компании', 'Решения', 'Отрасли', 'Портфолио', 'Пресс-центр', 'Контакты'])

        for item in first_level_menu:
            print(item.locate().text)
            item.hover()
            time.sleep(SLEEP_TIME)


    def hover_wait_and_click_element(menu, el_name):
        menu.hover().wait_until(browser.element(el_name).should(be.clickable))
        time.sleep(SLEEP_TIME)
        m = browser.element(el_name)
        m.should(be.clickable)
        m.hover()
        time.sleep(SLEEP_TIME)
        m.click()
        time.sleep(SLEEP_TIME2)

    def hover_wait_and_click_element_and_subelement(menu, el_name, sub_name):
        menu.hover().wait_until(browser.element(el_name).should(be.clickable))
        time.sleep(SLEEP_TIME)
        m = browser.element(el_name)
        m.should(be.clickable)
        m.hover()
        time.sleep(SLEEP_TIME)
        m2 = browser.element(sub_name)
        m2.should(be.clickable)
        m2.hover()
        time.sleep(SLEEP_TIME)
        m2.click()
        time.sleep(SLEEP_TIME2)

    def hover_wait_and_click_element_simple(menu):
        menu.hover()
        time.sleep(SLEEP_TIME)
        menu.click()
        time.sleep(SLEEP_TIME2)

    def leaf_over_bottom_blocks():
        browser.element('.callback-footer').perform(command.js.scroll_into_view)
        time.sleep(SLEEP_TIME)
        vpravo = browser.element('.c-next, .preview-next')
        for i in range(4):
            vpravo.click()
            time.sleep(SLEEP_TIME)
        browser.element('.swiper-slide-active').hover()
        time.sleep(SLEEP_TIME2)
        browser.element('.swiper-slide-next').hover()
        time.sleep(SLEEP_TIME2)

    def go_back_main_page():
        browser.element('[href="/"]').should(be.clickable).click()
        time.sleep(SLEEP_TIME2)

    browser: Browser = setup_browser
    base_url = os.getenv('BASE_URL')

    with allure.step("ТС2.1. Открыть главную страницу"):
        browser.open(f"{base_url}/")
        assert browser.element('.page .company_about').element('h1').should(have.exact_text('Софт Компани — цифровой системный интегратор.'))

    with allure.step("ТС2.2. Пройти по верхнему меню наведением курсора мыши"):
        go_throw_main_menu()


    with allure.step("ТС2.3. Пройти по избранным пунктам подменю"):
        # О компании
        menu = browser.element('.js-first-level > [href="/about/"]')
        elem_name = '.js-first-level .js-second-level'

        with allure.step("Открыть страницу 'Компания'"):
            pass
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Компания'))

        with allure.step("Открыть страницу 'Отзывы'"):
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/opinions/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Отзывы'))

        with allure.step("Открыть страницу 'Лицензии'"):
            pass
            # hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/certificates/"]')
            # assert browser.element('.controls-page-box .h1').should(have.exact_text('Лицензии'))

        with allure.step("Открыть страницу 'Карьера'"):
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/career/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Карьера'))

        with allure.step("Открыть страницу 'Политика конфиденциальности'"):
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/politika-konfidentsialnosti/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Политика конфиденциальности'))

        with allure.step("Сделать скриншот страницы 'Политика конфиденциальности'"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="politika_konfidentsialnosti", attachment_type=AttachmentType.PNG)

        # Решения
        menu = browser.element('.js-first-level > [href="/solutions/"]').should(be.clickable)
        elem_name = '.js-first-level .js-second-level'

        with allure.step("Открыть страницу 'Разработка ПО и автоматизация процессов'"):
            hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/razrabotka-po/"]',
                         f'{elem_name} [href="/solutions/razrabotka-po/razrabotka-programmnogo-obespecheniya/"]')
            assert browser.element('.solution-element-title').should(have.exact_text('Разработка ПО и автоматизация процессов'))

        with allure.step("Открыть страницу 'Управление технологическими процессами (УТП)''"):
            hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/"]',
                         f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/upravlenie-tekhnologicheskimi-protsessami-utp/"]')
            assert browser.element('.solution-element-title').should(have.exact_text('Управление технологическими процессами (УТП)'))

        # Отрасли
        menu = browser.element('.js-first-level > [href="/branch/"]').should(be.clickable)
        elem_name = '.js-first-level .js-second-level'

        with allure.step("Открыть страницу 'Государственный сектор'"):
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/gosudarstvennyy-sektor/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Государственный сектор'))

        with allure.step("Открыть страницу 'Транспорт и логистика'"):
            hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/transport-i-logistika/"]')
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Транспорт и логистика'))

        # Портфолио, Пресс-центр, Контакты
        with allure.step("Открыть страницу 'Клиенты'"):
            menu = browser.element('.js-first-level > [href="/clients/"]').should(be.clickable)
            hover_wait_and_click_element_simple(menu)
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Клиенты'))

        with allure.step("Открыть страницу 'Новости'"):
            menu = browser.element('.js-first-level > [href="/press-center/"]').should(be.clickable)
            hover_wait_and_click_element_simple(menu)
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Новости'))

        with allure.step("Открыть страницу 'Контакты'"):
            menu = browser.element('.js-first-level > [href="/contacts/"]').should(be.clickable)
            hover_wait_and_click_element_simple(menu)
            assert browser.element('.controls-page-box .h1').should(have.exact_text('Контакты'))

    with allure.step("ТС2.4. Пролистать блоки в разделе 'Клиенты и партнёры' внизу главной страницы"):
        go_back_main_page()
        leaf_over_bottom_blocks()

        with allure.step("ТС2.5. Сделать скриншот"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="bottom_blocks", attachment_type=AttachmentType.PNG)

    go_back_main_page()

    with allure.step("Прикрепить к allure-отчёту вложения (attachments): TEXT, HTML, JSON"):
        allure.attach("Text content: это прикреплённый текст", name="Text", attachment_type=attachment_type.TEXT)
        allure.attach("<h1>Hello, world</h1><h2>это прикреплённый текст</h2>", name="Html", attachment_type=attachment_type.HTML)
        allure.attach(json.dumps({"Тест": "ТС2", "Описание": "Проверка работоспособности пунктов и подпунктов главного меню"}), name="Json", attachment_type=attachment_type.JSON)
