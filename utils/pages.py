from conftest import PRODUCT_PAGE_URL_1, MAIN_PAGE_URL
from pages.mainpage import MainPage
from pages.product_page import ProductPage


def product_page_close_ad(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL_1)
    product_page.close_ad()


def main_page_close_ad(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.close_ad()
