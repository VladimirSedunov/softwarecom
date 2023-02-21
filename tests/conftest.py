import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.base_url = "https://softwarecom.ru"
    browser.config.window_width = 1900
    browser.config.window_height = 1000
    # browser.config.browser_name = 'firefox'
    # browser.config.hold_browser_open = True

    yield

    # with allure.step("Пример из QA-guru вложений (attachments): TEXT, HTML, JSON"):
    #     attach.add_html(browser)
    #     attach.add_screenshot(browser)
    #     attach.add_logs(browser)
    #     attach.add_video(browser)

    # browser.quit()



