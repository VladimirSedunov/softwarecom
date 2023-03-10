
# import os

import pytest
# from dotenv.main import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
# from dotenv import load_dotenv

from utils import attach

DEFAULT_BROWSER_VERSION = "95.0"


# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='93.0'
#     )


# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()


@pytest.fixture(scope='function')
# @pytest.fixture(scope='session', autouse=True)
# def setup_browser(request):
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    # browser_version = DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="http://10.155.56.61:4444/wd/hub",
        options=options
    )

    print(4)

    browser = Browser(Config(driver))

    browser.config.base_url = "https://softwarecom.ru"
    browser.config.window_width = 1900
    browser.config.window_height = 1000

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()




# import pytest
# from selene.support.shared import browser
#
#
# @pytest.fixture(scope="session", autouse=True)
# def browser_management():
#     browser.config.base_url = "https://softwarecom.ru"
#     browser.config.window_width = 1900
#     browser.config.window_height = 1000
#     # browser.config.browser_name = 'firefox'
#     # browser.config.hold_browser_open = True
#
#     yield
#
#     # with allure.step("Пример из QA-guru вложений (attachments): TEXT, HTML, JSON"):
#     #     attach.add_html(browser)
#     #     attach.add_screenshot(browser)
#     #     attach.add_logs(browser)
#     #     attach.add_video(browser)
#
#     # browser.quit()
#
##########################################################################################
