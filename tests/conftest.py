import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
# from selene import Browser, Config

from tests.utils import attach

DEFAULT_BROWSER_VERSION = '95.0'
DEFAULT_BROWSER = 'chrome'
DEFAULT_WINDOW_SIZE = '1024x768'


# это хук
def pytest_addoption(parser):
    parser.addoption('--browser_version', default='96.0')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--window-size', default='1920x1080')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(scope='module', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    # print(f'browser_version={browser_version}')
    # browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    browser_ = request.config.getoption('--browser')
    # browser_ = browser_ if browser_ != "" else DEFAULT_BROWSER

    videoScreenSize = str(request.config.getoption('--window-size'))
    window_size = videoScreenSize.replace('x', ',').split(',')

    options = Options()

    selenoid_capabilities = {
        "browserName": browser_,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "videoScreenSize": videoScreenSize
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="http://10.155.56.61:4444/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = int(window_size[0])
    browser.config.window_height = int(window_size[1])

    # browser.config.base_url = 'https://softwarecom.ru'

    yield browser

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)

    with allure.step("Видеозапись теста"):
        attach.add_video(browser)

    browser.quit()
