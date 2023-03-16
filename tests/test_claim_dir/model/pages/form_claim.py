from dataclasses import dataclass
from selene.support.conditions import have, be

from tests.test_claim_dir.data.claim_data import Claim


@dataclass
class Form_Claim:
    orderForm_CSS = '#orderForm'
    fio: str
    phone: str
    email: str
    text: str
    pers_data_agree: bool
    send_button: str

    def __init__(self):
        self.clear()

    def clear(self):
        self.fio = ''
        self.phone = ''
        self.email = ''
        self.text = ''
        self.pers_data_agree = True

    def fill(self, claim: Claim, browser):
        browser.element(self.orderForm_CSS).should(be.clickable)
        feedback_form = browser.element(self.orderForm_CSS)
        feedback_form.element('[name=fio]').should(be.enabled).set_value(claim.fio)
        feedback_form.element('[name=phone]').should(be.enabled).set_value(claim.phone)
        feedback_form.element('[name=email]').should(be.enabled).set_value(claim.email)
        feedback_form.element('[name=text]').should(be.enabled).set_value(claim.text)
        if claim.pers_data_agree != len(feedback_form.all('.agreeDiv.selected').should(be.existing)) > 0:
            feedback_form.element('.agreeDiv').should(be.clickable).click()

    def submit(self, browser):
        browser.element(self.orderForm_CSS).element('[type=submit][name=send]').should(be.clickable).click()

    def check(self, claim: Claim, browser):
        if not claim.is_error:
            browser.element('.msg-wrap').should(have.exact_text(claim.expected_result_message))
        else:
            feedback_form = browser.element(self.orderForm_CSS)
            feedback_form.element('.js-error').should(have.exact_text(claim.expected_result_message))
