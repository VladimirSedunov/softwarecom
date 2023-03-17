import allure
import pytest
from dotenv import load_dotenv
# from dotenv.main import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
# from selene import Browser, Config

from tests.utils import attach

DEFAULT_BROWSER_VERSION = '95.0'


# это хук
def pytest_addoption(parser):
    parser.addoption('--browser_version', default='96.0')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def setup_browser(request):

    browser_version = request.config.getoption('--browser_version')
    print(f'browser_version={browser_version}')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        # "browserName": "firefox",
        "browserVersion": browser_version,
        # "browserVersion": '101.0',
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

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)

    with allure.step("Видеозапись теста"):
        attach.add_video(browser)

    browser.quit()
