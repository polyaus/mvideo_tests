import pytest

MAIN_PAGE_URL = "https://www.mvideo.ru/"
LOGIN_PAGE_URL = "https://www.mvideo.ru/login"
PRODUCT_PAGE_URL_1 = "https://www.mvideo.ru/products/smartfon-apple-iphone-12-pro-max-512gb-gold-mgdk3ru-a-30052922"
PRODUCT_PAGE_URL_2 = "https://www.mvideo.ru/products/smartfon-xiaomi-redmi-9a-32gb-peacock-green-30051226"
FAVORITE_PAGE_URL = "https://www.mvideo.ru/wish-list"


@pytest.fixture(scope="function")
def main_page_url():
    return "https://www.mvideo.ru/"


def login_page_url_raw():
    return "https://www.mvideo.ru/login"


@pytest.fixture(scope="function")
def login_page_url():
    return login_page_url_raw()


@pytest.fixture(scope="function")
def product_page_url():
    return PRODUCT_PAGE_URL_1


@pytest.fixture(scope="function")
def product_page_url_2():
    return PRODUCT_PAGE_URL_2


def favorite_page_url_raw():
    return "https://www.mvideo.ru/wish-list"


@pytest.fixture(scope="function")
def favorite_page_url():
    return favorite_page_url_raw()
