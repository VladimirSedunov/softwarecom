import allure
import pytest
from dotenv.main import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from tests.utils import attach

DEFAULT_BROWSER_VERSION = '95.0'

# browser.config.window_width = 1900
# browser.config.window_height = 1000


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='95.0')
    # parser.addoption('--window-size', default='1920,1080')


# создал пустой файл с переменными среды '.env'
# функция pytest_addoption добавила переменную среды '--browser_version'
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(scope='module', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    print(f'browser_version={browser_version}')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        # "browserSize": "1920x1080",
        # "videoScreenSize": "1920x1080",
        # "screenResolution": "1280x1024x24",
        # "windowSize": "1280,1024",
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

    browser = Browser(Config(driver))

    yield browser

    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)

    # with allure.step("Видеозапись теста"):
    #     attach.add_video(browser)

    browser.quit()
