import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=chrome_options)

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def main_page_url():
    return "https://www.mvideo.ru/"


@pytest.fixture(scope="function")
def login_page_url():
    return "https://www.mvideo.ru/login"


@pytest.fixture(scope="function")
def product_page_url():
    return "https://www.mvideo.ru/products/smartfon-apple-iphone-12-pro-max-512gb-gold-mgdk3ru-a-30052922"


@pytest.fixture(scope="function")
def product_page_url_2():
    return "https://www.mvideo.ru/products/smartfon-xiaomi-redmi-9a-32gb-peacock-green-30051226"


@pytest.fixture(scope="function")
def favorite_page_url():
    return "https://www.mvideo.ru/wish-list"
