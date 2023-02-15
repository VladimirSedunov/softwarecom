from dataclasses import dataclass

from selene.support.conditions import have, be
from selene.support.shared import browser


@dataclass
class Form_Main:
    endpoint: str
    selector_menu: str
    check_word: str
    selector_check_word: str
    claim_button: str

    def __init__(self):
        self.endpoint = '/about/'
        self.selector_check_word = '.controls-page-box .h1'
        self.check_word = 'Компания'
        self.claim_button = '.order-btn-popup'

    def open(self):
        browser.open(self.endpoint)

    def check(self):
        assert browser.element(self.selector_check_word).should(have.exact_text(self.check_word))

    def open_claim_form(self):
        browser.element(self.claim_button).should(be.clickable).click()
