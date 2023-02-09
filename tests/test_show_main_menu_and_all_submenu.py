import json
import time
import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene import command, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
# from selenium.webdriver import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from allure import attachment_type


# @allure.tag("web")
# @allure.label("owner", "eroshenkoam")
# @allure.feature("Задачи в репозитории")
# @allure.story("Авторизованный пользователь может создать задачу в репозитории")
# @allure.link("https://github.com", name="Testing")
@allure.severity(Severity.CRITICAL)
@pytest.mark.demo
def test_show_main_menu_and_all_submenu():
    # allure.dynamic.severity(Severity.CRITICAL)
    with allure.step("Открываем главную страницу"):
        browser.open("/")
        assert browser.element('.page .company_about').element('h1').should(have.exact_text('Софт Компани — цифровой системный интегратор.'))

    with allure.step("Проходим по верхнему меню"):
        go_throw_main_menu()

    with allure.step("Проходим по всем подменю"):

        # О компании
        menu = browser.element('.js-first-level > [href="/about/"]')
        elem_name = '.js-first-level .js-second-level'

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Компания'))

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/opinions/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Отзывы'))

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/certificates/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Лицензии'))

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/career/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Карьера'))

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/politika-konfidentsialnosti/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Политика конфиденциальности'))

        with allure.step("Делаем скриншот"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="politika_konfidentsialnosti", attachment_type=AttachmentType.PNG)

        # Решения
        menu = browser.element('.js-first-level > [href="/solutions/"]')
        elem_name = '.js-first-level .js-second-level'

        hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/razrabotka-po/"]',
                     f'{elem_name} [href="/solutions/razrabotka-po/razrabotka-programmnogo-obespecheniya/"]')
        assert s('.solution-element-title').should(have.exact_text('Разработка ПО и автоматизация процессов'))

        hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/"]',
                     f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/upravlenie-tekhnologicheskimi-protsessami-utp/"]')
        assert s('.solution-element-title').should(have.exact_text('Управление технологическими процессами (УТП)'))

        # Отрасли
        menu = browser.element('.js-first-level > [href="/branch/"]')
        elem_name = '.js-first-level .js-second-level'
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/gosudarstvennyy-sektor/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Государственный сектор'))

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/transport-i-logistika/"]')
        assert s('.controls-page-box .h1').should(have.exact_text('Транспорт и логистика'))

        # Портфолио, Пресс-центр, Контакты
        menu = browser.element('.js-first-level > [href="/clients/"]')
        hover_wait_and_click_element_simple(menu)
        assert s('.controls-page-box .h1').should(have.exact_text('Клиенты'))

        menu = browser.element('.js-first-level > [href="/press-center/"]')
        hover_wait_and_click_element_simple(menu)
        assert s('.controls-page-box .h1').should(have.exact_text('Новости'))

        menu = browser.element('.js-first-level > [href="/contacts/"]')
        hover_wait_and_click_element_simple(menu)
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты'))

    with allure.step("Листаем блоки в разделе 'Клиенты и партнёры' внизу страницы"):
        go_back_main_page()
        leaf_over_bottom_blocks()

        with allure.step("Делаем скриншот"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="bottom_blocks", attachment_type=AttachmentType.PNG)

    go_back_main_page()

    with allure.step("Пример вложений (attachments): TEXT, HTML, JSON"):
        allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
        allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
        allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)


SLEEP_TIME = 1.0
SLEEP_TIME2 = 2


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
    time.sleep(1)
    vpravo = browser.element('.c-next, .preview-next')
    for i in range(4):
        vpravo.click()
        time.sleep(SLEEP_TIME)
    browser.element('.swiper-slide-active').hover()
    time.sleep(SLEEP_TIME2)
    browser.element('.swiper-slide-next').hover()
    time.sleep(SLEEP_TIME2)


def go_throw_main_menu():
    first_level_menu = browser.all('.js-first-level')
    list_ = []
    for item in first_level_menu:
        list_.append(item.locate().text)
    assert len(first_level_menu) == 6
    assert (list_ == ['О компании', 'Решения', 'Отрасли', 'Портфолио', 'Пресс-центр', 'Контакты'])

    for item in first_level_menu:
        # print(item.locate().text)
        item.hover()
        time.sleep(SLEEP_TIME)


def go_back_main_page():
    browser.element('[href="/"]').should(be.clickable).click()
    time.sleep(SLEEP_TIME2)

