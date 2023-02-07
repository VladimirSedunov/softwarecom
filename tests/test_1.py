import time

import allure
from selene import command, be, have
from selene.support.shared import browser
# from selene.support.shared.jquery_style import s
# from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_show_all_menu():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Проходим по верхнему меню"):
        first_level_menu = browser.all('.js-first-level')
        # после отладки раскомментировать
        for item in first_level_menu:
            # print(item.locate().text)
            item.hover()
            time.sleep(1)

    with allure.step("О компании - проходим по всем подменю"):
        menu = browser.element('.js-first-level > [href="/about/"]')
        menu.hover()
        time.sleep(2)

        elem_name = '.js-first-level .js-second-level'
        menu.hover()
        browser.element(f'{elem_name} > [href="/about/"]').click()
        time.sleep(2)
        menu.hover()
        browser.element(f'{elem_name} > [href="/about/opinions/"]').click()
        time.sleep(2)
        menu.hover()
        browser.element(f'{elem_name} > [href="/about/certificates/"]').click()
        time.sleep(2)
        menu.hover()
        browser.element(f'{elem_name} > [href="/about/career/"]').click()
        time.sleep(2)
        menu.hover()
        browser.element(f'{elem_name} > [href="/about/politika-konfidentsialnosti/"]').click()
        time.sleep(2)

        first_level_menu[1].hover()
        time.sleep(1)
        browser.element('.js-second-level [href="/solutions/razrabotka-po/"]').should(be.visible).hover()
        time.sleep(1)
        browser.element('.js-second-level [href="/solutions/razrabotka-po/razrabotka-programmnogo-obespecheniya/"]').click()
        time.sleep(1)

        first_level_menu[1].hover()
        time.sleep(1)
        browser.element('.js-second-level [href="/solutions/produkty-i-korobochnye-resheniya/"]').hover()
        time.sleep(1)
        browser.element('.js-second-level [href="/solutions/produkty-i-korobochnye-resheniya/upravlenie-tekhnologicheskimi-protsessami-utp/"]').click()
        time.sleep(1)

        first_level_menu[2].hover()
        time.sleep(1)
        browser.element('.js-second-level [href="/branch/transport-i-logistika/"]').should(be.visible).hover()
        browser.element('.js-second-level [href="/branch/transport-i-logistika/"]').click()
        time.sleep(2)

        browser.element('.nav-three [href="/about/"]').click()
        time.sleep(1)
        time.sleep(1)
        browser.element('.nav-to [href="/solutions/razrabotka-po/"]').click()
        time.sleep(1)
        browser.element('.nav-to [href="/solutions/produkty-i-korobochnye-resheniya/"]').click()
        time.sleep(1)
        browser.element('.nav-three [href="/about/certificates/"]').click()
        time.sleep(1)
        browser.element('.nav-three [href="/solutions/it-uslugi-i-podderzhka/""]').click()
        time.sleep(1)


    # после отладки раскомментировать
    with allure.step("Идём в низ страницы"):
        browser.element('.callback-footer').perform(command.js.scroll_into_view)
        time.sleep(1)

    with allure.step("Листаем блоки в разделе 'Клиенты и партнёры'"):
        vpravo = browser.element('.c-next, .preview-next')
        for i in range(4):
            vpravo.click()
            time.sleep(1)
        browser.element('.swiper-slide-active').hover()
        time.sleep(2)
        browser.element('.swiper-slide-next').hover()
        time.sleep(2)
