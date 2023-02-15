from selene import have
from selene.support.shared import browser


class Checkbox:

    def __int__(self, locator, value):
        self.locator = locator
        self.value = value

    @staticmethod
    def click_checkbox(locator, value):
        browser.all(locator).element_by(have.text(value)).click()
