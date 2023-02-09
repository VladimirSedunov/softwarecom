import allure
import pytest
from selene.support.shared import browser
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    # browser.config.browser_name = 'firefox'
    # browser.config.hold_browser_open = True
    browser.config.base_url = "https://softwarecom.ru"
    browser.config.window_width = 1900
    browser.config.window_height = 1000

    yield

    # with allure.step("Пример из QA-guru вложений (attachments): TEXT, HTML, JSON"):
    #     attach.add_html(browser)
    #     attach.add_screenshot(browser)
    #     attach.add_logs(browser)
    #     attach.add_video(browser)

    # browser.quit()
