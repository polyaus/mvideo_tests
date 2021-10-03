from conftest import PRODUCT_PAGE_URL_1, PRODUCT_PAGE_URL_2
from pages.product_page import ProductPage


def test_favorite_list_is_empty(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
    product_page.favorite_is_empty()


def test_product_in_favorite_list(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()


def test_two_product_in_favorite_list(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    product_page_2 = ProductPage(browser, PRODUCT_PAGE_URL_2)
    product_page_2.add_favorite_product()
    product_page_2.in_favorite_list_two_products()


def test_delete_product_from_favorite_list_on_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()
    product_page.click_body()
    product_page.del_favorite_product()
    product_page.favorite_is_empty()


def test_delete_two_product_from_favorite_list_on_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    product_page_2 = ProductPage(browser, PRODUCT_PAGE_URL_2)
    product_page_2.add_favorite_product()
    product_page_2.in_favorite_list_two_products()

    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.del_favorite_product()
    product_page.in_favorite_list_one_product()

    product_page_2 = ProductPage(browser, PRODUCT_PAGE_URL_2)
    product_page_2.del_favorite_product()
    product_page_2.favorite_is_empty()
