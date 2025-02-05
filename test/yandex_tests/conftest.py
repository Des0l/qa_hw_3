import pytest
from selene import browser


@pytest.fixture(autouse=True, scope = "function")
def browser_test_setup():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://ya.ru')
    yield
    browser.quit()
