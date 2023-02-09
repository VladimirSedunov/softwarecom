import random
import time
import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.controls import Dropdown


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
def test_Фильтрация_Клиентов_В_Портфолио():
    with allure.step("Открываем меню Портфолио"):
        browser.open("/clients/")
        assert s('.controls-page-box .h1').should(have.exact_text('Клиенты')) is not None


        for j in range(10):
            dropdown_otrasl_elem = browser.all('.select-title').element_by(have.exact_text('Отрасль')).element(
                '..').element('.select-section')
            dropdown_otrasl_elem.click()
            time.sleep(2)

            all_elem = dropdown_otrasl_elem.all('#branchFilter > option')
            i = random.randint(0, len(all_elem) - 1)
            all_elem[i].click()

            time.sleep(2)



        # e = browser.all('.select-title').element_by(have.exact_text('Услуга')).element('..')
        # print(e.locate().get_attribute('class'))
        #
        # ops = e.element('.select-section #solutionFilter').all('option')
        # for item in ops:
        #     print(item.locate().text)

