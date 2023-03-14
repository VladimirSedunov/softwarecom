from dataclasses import dataclass
from selene.support.conditions import have, be


@dataclass
class Form_Main():
    base_url: str
    endpoint: str
    selector_menu: str
    check_word: str
    selector_check_word: str
    claim_button: str

    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoint = f'{self.base_url}/about/'
        self.selector_check_word = '.controls-page-box .h1'
        self.check_word = 'Компания'
        self.claim_button = '.order-btn-popup'

    def open(self, browser):
        browser.open(self.endpoint)

    def check(self, browser):
        assert browser.element(self.selector_check_word).should(have.exact_text(self.check_word))

    def open_claim_form(self, browser):
        browser.element(self.claim_button).should(be.clickable).click()
