from selene import have, be
import datetime
import sys
from selenium.webdriver import Keys
from utils import config


class Dropdown:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select(self, value):
        self.element.click()
        self.elements.element_by(have.exact_text(value)).click()


class Checkbox:

    def __init__(self, element):
        self.element = element

    def set(self, list_value):
        for hobby in list_value:
            self.element.element_by(have.exact_text(hobby.name)).click()


class Datepicker:

    def __init__(self, element):
        self.element = element

    def set(self, date: datetime.date):
        self.element.send_keys(
            Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a').type(
            date.strftime(config.datetime_input_format)).press_enter()


class InputTab:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def set_value(self, value):
        self.element.type(value)
        self.elements.element_by(have.exact_text(value)).should(be.visible)
        self.element.press_tab()


class Radio:

    def __init__(self, element):
        self.element = element

    def set(self, value):
        self.element.element_by(have.value(value)).element('..').click()
