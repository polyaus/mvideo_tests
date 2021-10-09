from conftest import PRODUCT_PAGE_URL_1, PRODUCT_PAGE_URL_2
from pages.product_page import ProductPage
from utils.browsers import build_browser
from utils.pages import product_page_close_ad


class TestsForProductPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()
        product_page_close_ad(cls.browser)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        product_page = ProductPage(self.browser, PRODUCT_PAGE_URL_1)
        product_page.del_product_from_favorites()

        product_page_2 = ProductPage(self.browser, PRODUCT_PAGE_URL_2)
        product_page_2.del_product_from_favorites()

        product_page_2.favorites_is_empty()

    def test_favorite_list_is_empty(self, product_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorites_is_empty()

    def test_product_in_favorite_list(self, product_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorites_is_empty()
        product_page.add_product_in_favorites()
        product_page.one_product_in_favorites()

    def test_two_product_in_favorite_list(self, product_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorites_is_empty()
        product_page.add_product_in_favorites()
        product_page.one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.add_product_in_favorites()
        product_page_2.two_products_in_favorites()

    def test_delete_product_from_favorite_list_on_product_page(self, product_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorites_is_empty()
        product_page.add_product_in_favorites()
        product_page.one_product_in_favorites()
        product_page.click_body()
        product_page.del_product_from_favorites()
        product_page.favorites_is_empty()

    def test_delete_two_product_from_favorite_list_on_product_page(self, product_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorites_is_empty()
        product_page.add_product_in_favorites()
        product_page.one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.add_product_in_favorites()
        product_page_2.two_products_in_favorites()

        product_page = ProductPage(self.browser, product_page_url)
        product_page.del_product_from_favorites()
        product_page.one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.del_product_from_favorites()
        product_page_2.favorites_is_empty()
