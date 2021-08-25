from pages.favorite_page import FavoritePage
from pages.product_page import ProductPage


def test_favorite_list_is_empty(browser, product_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()


def test_product_in_favorite_list(browser, product_page_url, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()
