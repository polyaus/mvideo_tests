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


@pytest.fixture(scope="function")
def product_page_url():
    return "https://www.mvideo.ru/products/smartfon-apple-iphone-12-pro-max-512gb-gold-mgdk3ru-a-30052922"
