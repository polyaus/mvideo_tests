from conftest import PRODUCT_PAGE_URL_1
from pages.product_page import ProductPage


def product_page_close_ad(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()
