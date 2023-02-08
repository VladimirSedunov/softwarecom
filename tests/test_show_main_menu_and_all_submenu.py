import time
import allure
from selene import command, be, have
from selene.support.shared import browser
# from selene.support.shared.jquery_style import s
# from selenium.webdriver import Keys
# from selenium.webdriver.common.action_chains import ActionChains


def test_show_main_menu_and_all_submenu():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Проходим по верхнему меню"):
        go_throw_main_menu()

    with allure.step("Проходим по всем подменю"):

        menu = browser.element('.js-first-level > [href="/about/"]')
        elem_name = '.js-first-level .js-second-level'

        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/"]')
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/opinions/"]')
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/certificates/"]')
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/career/"]')
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/about/politika-konfidentsialnosti/"]')

        menu = browser.element('.js-first-level > [href="/solutions/"]')
        elem_name = '.js-first-level .js-second-level'

        hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/razrabotka-po/"]',
                     f'{elem_name} [href="/solutions/razrabotka-po/razrabotka-programmnogo-obespecheniya/"]')

        hover_wait_and_click_element_and_subelement(menu, f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/"]',
                     f'{elem_name} [href="/solutions/produkty-i-korobochnye-resheniya/upravlenie-tekhnologicheskimi-protsessami-utp/"]')

        menu = browser.element('.js-first-level > [href="/branch/"]')
        elem_name = '.js-first-level .js-second-level'
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/gosudarstvennyy-sektor/"]')
        hover_wait_and_click_element(menu, f'{elem_name} > [href="/branch/transport-i-logistika/"]')

        menu = browser.element('.js-first-level > [href="/clients/"]')
        hover_wait_and_click_element_simple(menu)
        menu = browser.element('.js-first-level > [href="/press-center/"]')
        hover_wait_and_click_element_simple(menu)
        menu = browser.element('.js-first-level > [href="/contacts/"]')
        hover_wait_and_click_element_simple(menu)


    with allure.step("Листаем блоки в разделе 'Клиенты и партнёры' внизу страницы"):
        go_back_main_page()
        leaf_over_bottom_blocks()


SLEEP_TIME = 0.5
SLEEP_TIME2 = 2


def hover_wait_and_click_element(menu, el_name):
    menu.hover()
    time.sleep(SLEEP_TIME)
    m = browser.element(el_name).should(be.clickable)
    m.hover()
    time.sleep(SLEEP_TIME)
    m.click()
    time.sleep(SLEEP_TIME2)


def hover_wait_and_click_element_and_subelement(menu, el_name, sub_name):
    menu.hover()
    time.sleep(SLEEP_TIME)
    browser.element(el_name).should(be.visible).hover()
    time.sleep(SLEEP_TIME)
    browser.element(sub_name).click()   # ещё hover() добавить сюда ?
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
        time.sleep(1)
    browser.element('.swiper-slide-active').hover()
    time.sleep(2)
    browser.element('.swiper-slide-next').hover()
    time.sleep(2)


def go_throw_main_menu():
    first_level_menu = browser.all('.js-first-level')
    for item in first_level_menu:
        # print(item.locate().text)
        item.hover()
        time.sleep(1)


def go_back_main_page():
    browser.element('[href="/"]').should(be.clickable).click()

