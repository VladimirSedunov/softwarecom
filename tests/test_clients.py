import os
import time
import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene.support.conditions import have, be
from selene.core.entity import Browser

from tests.utils import attach

SLEEP_TIME = 0.5


@allure.title('ТС3. Фильтрация клиентов в портфолио')
@allure.severity(Severity.NORMAL)
# @pytest.mark.skip
@pytest.mark.jenkins_ok
def test_Фильтрация_Клиентов_В_Портфолио(setup_browser):
    browser: Browser = setup_browser
    # base_url = os.getenv('BASE_URL')

    with allure.step("ТС3.1. Открыть страницу Портфолио"):
        # browser.open(f"{base_url}/clients/")
        browser.open(f"/clients/")
        assert browser.element('.controls-page-box .h1').should(have.exact_text('Клиенты')) is not None
    try:
        with allure.step("ТС3.2. Цикл по всем отраслям и услугам"):
            print('')
            browser.all('#branchFilter > option').with_(timeout=9.0).wait_until(have.size_greater_than_or_equal(1))
            otrasli = browser.all('#branchFilter > option')
            assert len(otrasli) > 0

            for j in range(0, len(otrasli)):
                dropdown_otrasl_elem = browser.all('.select-title').element_by(have.exact_text('Отрасль')).element('..').element('.select-section').should(
                    be.clickable)
                dropdown_otrasl_elem.click()
                time.sleep(SLEEP_TIME)

                browser.all('.ik_select_block').with_(timeout=9.0).wait_until(have.size_greater_than_or_equal(1))

                select_block = browser.all('.ik_select_block')[1].all('.ik_select_option')

                time.sleep(1)
                by_text = select_block[j].locate().text
                print(f'Отрасль: {by_text}')
                select_block[j].element('..').click()
                time.sleep(SLEEP_TIME)

                uslugi = browser.all('#solutionFilter > option')
                list_nums = list(range(0, len(uslugi)))
                list_nums.append(0)
                list_nums.pop(0)
                for j_usluga in list_nums:
                    dropdown_usluga_elem = browser.all('.select-title').element_by(have.exact_text('Услуга')).element('..').element('.select-section').should(
                        be.clickable)
                    dropdown_usluga_elem.click()
                    time.sleep(SLEEP_TIME)

                    select_block_usluga = browser.all('.ik_select_block')[1].all('.ik_select_option')

                    by_text_usluga = select_block_usluga[j_usluga].locate().text

                    # print(f'         Услуга: {by_text_usluga.ljust(30)}      {str(len(browser.all(".client-item"))).rjust(5)}')

                    select_block_usluga[j_usluga].element('..').click()
                    time.sleep(SLEEP_TIME)
                    if by_text_usluga.upper() != 'Все'.upper():
                        print(f'         Услуга: {by_text_usluga.ljust(30)}      {str(len(browser.all(".client-item"))).rjust(5)}')

    except:
        with allure.step("ТС3.3. Сделать скриншот"):
            allure.attach(browser.driver.get_screenshot_as_png(), name="bottom_blocks", attachment_type=AttachmentType.PNG)
        assert False

    finally:
        with allure.step("Видеозапись теста"):
            print('finally')
            attach.add_video(browser)
