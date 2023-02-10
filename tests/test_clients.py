import random
import time
import allure
import pytest
from allure_commons.types import Severity
from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.controls import Dropdown


@allure.severity(Severity.NORMAL)
@pytest.mark.demo
def test_Фильтрация_Клиентов_В_Портфолио():
    with allure.step("Открываем меню Портфолио"):
        browser.open("/clients/")
        assert s('.controls-page-box .h1').should(have.exact_text('Клиенты')) is not None

    print()
    with allure.step("Цикл по всем отраслям"):
        otrasli = browser.all('#branchFilter > option')
        for j in range(0, len(otrasli)):
            dropdown_otrasl_elem = browser.all('.select-title').element_by(have.exact_text('Отрасль')).element('..').element('.select-section')
            dropdown_otrasl_elem.click()
            time.sleep(1)
            select_block = browser.all('.ik_select_block')[1].all('.ik_select_option')
            by_text = select_block[j].locate().text
            print(f'Отрасль: {by_text}')
            select_block[j].element('..').click()
            time.sleep(1)


            uslugi = browser.all('#solutionFilter > option')
            for j_usluga in range(0, len(uslugi)):
                dropdown_usluga_elem = browser.all('.select-title').element_by(have.exact_text('Услуга')).element('..').element('.select-section')
                dropdown_usluga_elem.click()
                time.sleep(1)
                select_block_usluga = browser.all('.ik_select_block')[1].all('.ik_select_option')
                by_text_usluga = select_block_usluga[j_usluga].locate().text
                print(f'         Услуга: {by_text_usluga}')
                select_block_usluga[j_usluga].element('..').click()
                time.sleep(1)






        # for j in range(0, 1):
        #     print(j)
        #     dropdown_otrasl_elem = browser.all('.select-title').element_by(have.exact_text('Отрасль')).element('..').element('.select-section')
        #     dropdown_otrasl_elem.click()
        #     all_elem = dropdown_otrasl_elem.all('#branchFilter > option')
        #     print(all_elem[j].locate().text)
        #     n_all_elem = len(all_elem)
        #     # i = random.randint(0, len(all_elem) - 1)
        #     all_elem[j].should(be.clickable).click()
        #     print(dropdown_otrasl_elem.element('.ik_select_link_text').locate().text)
        #     time.sleep(2)



        # e = browser.all('.select-title').element_by(have.exact_text('Услуга')).element('..')
        # print(e.locate().get_attribute('class'))
        #
        # ops = e.element('.select-section #solutionFilter').all('option')
        # for item in ops:
        #     print(item.locate().text)

