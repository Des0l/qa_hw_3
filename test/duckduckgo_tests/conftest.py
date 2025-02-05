import pytest
from selene import browser


@pytest.fixture(autouse=True, scope = "function")
def browser_test_setup():
    browser.open("https://duckduckgo.com")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()
