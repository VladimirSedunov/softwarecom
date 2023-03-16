from selene.support.conditions import be


class Textbox:

    def __int__(self, locator, value):
        self.locator = locator
        self.value = value

    @staticmethod
    def set_text(form, locator, value):
        form.element(locator).should(be.enabled).set_value(value)
