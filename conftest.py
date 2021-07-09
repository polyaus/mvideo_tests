import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def main_page_url():
    return "https://www.mvideo.ru/"
