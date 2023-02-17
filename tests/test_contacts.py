import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
def test_Проверка_Контактных_Данных():

    real_address = '125190, Москва, Ленинградский проспект, 80к37, 5 этаж'
    real_email = 'E-mail: info@softwarecom.ru'
    real_phone = 'Tел. +7 (495) 983-05-48'

    with allure.step("ТС7.1. Открыть страницу 'Контакты'"):
        browser.open("/contacts/")
        assert s('.controls-page-box .h1').should(have.exact_text('Контакты')).should(be.existing)

    with allure.step("ТС7.2. Проверить наличие блока контактных данных"):
        contacts = s('.map-contacts--center').should(be.existing)
        lstr = contacts.locate().text.splitlines()

    with allure.step("ТС7.3. Проверить адрес, email и телефон"):
        assert len(lstr) >= 4, "В адресе меньше четырёх строк"

        address = f'{lstr[0]}, {lstr[1]}'
        email = f'{lstr[2]}'
        phone = f'{lstr[3]}'

        assert address == real_address, f'Адрес отличается от реального: "{real_address}"'
        assert email == real_email, f'E-mail отличается от реального: "{real_email}"'
        assert phone == real_phone, f'Телефон отличается от реального: "{real_phone}"'
