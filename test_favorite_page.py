from conftest import LOGIN_PAGE_URL, FAVORITE_PAGE_URL
from pages.favorite_page import FavoritePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.browsers import build_browser
from utils.pages import product_page_close_ad


class TestsWithoutLogin:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()
        product_page_close_ad(cls.browser)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        favorite_page = FavoritePage(self.browser, FAVORITE_PAGE_URL)
        favorite_page.delete_all_products_from_favorites()
        favorite_page.open()
        favorite_page.favorites_is_empty()

    def test_favorite_list_is_empty(self, favorite_page_url):
        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.favorites_is_empty()

    def test_add_product_to_fav(self, product_page_url, favorite_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

    def test_favorite_list_is_not_empty(self, product_page_url, favorite_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.favorites_is_not_empty()

    def test_delete_product_from_favorite_list(self, product_page_url, favorite_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()
        favorite_page.delete_one_product_from_favorites()
        favorite_page.favorites_is_empty_after_delete_products()

    def test_add_two_product_in_favorite_list(self, product_page_url, favorite_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.add_favorite_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_two_products_in_favorites()

    def test_delete_first_added_product_from_favorite_list(self, product_page_url, favorite_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.add_favorite_product()
        product_page_2.in_favorite_list_two_products()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.delete_first_added_product_in_favorites()

    def test_delete_all_two_products_from_favorite_list(self, product_page_url, favorite_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.add_favorite_product()
        product_page_2.in_favorite_list_two_products()

        favorite_page = FavoritePage(self.browser, FAVORITE_PAGE_URL)
        favorite_page.check_two_products_in_favorites()
        favorite_page.delete_all_products_from_favorites()
        favorite_page.favorites_is_empty_after_delete_products()


class TestUserCases:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()
        product_page_close_ad(cls.browser)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def teardown_method(self, method):
        login_page = LoginPage(self.browser, LOGIN_PAGE_URL)
        login_page.open_user_cabinet()
        login_page.user_logout()
        login_page.check_user_is_not_authorization()

        favorite_page = FavoritePage(self.browser, FAVORITE_PAGE_URL)
        favorite_page.delete_all_products_from_favorites()
        favorite_page.favorites_is_empty()

        login_page = LoginPage(self.browser, LOGIN_PAGE_URL)
        login_page.enter_user_data_for_authorization()
        login_page.check_user_is_authorization()

        favorite_page = FavoritePage(self.browser, FAVORITE_PAGE_URL)
        favorite_page.delete_all_products_from_favorites()
        favorite_page.favorites_is_empty_after_delete_products()

        login_page = LoginPage(self.browser, LOGIN_PAGE_URL)
        login_page.open_user_cabinet()
        login_page.user_logout()
        login_page.check_user_is_not_authorization()

    def test_authorization_after_add_one_product_in_favorite_list(self, product_page_url, login_page_url, favorite_page_url):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_form_authorization()
        login_page.enter_user_data_for_authorization()
        login_page.check_user_is_authorization()
        login_page.check_product_in_favorite_from_login_page()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

    def test_add_product_to_favorite_is_not_visible_outside(self, login_page_url, product_page_url, favorite_page_url):
        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_form_authorization()
        login_page.enter_user_data_for_authorization()
        login_page.open_user_cabinet()
        login_page.check_user_is_authorization()
        login_page.favorite_is_empty_from_login_page()

        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_user_cabinet()
        login_page.check_product_in_favorite_from_login_page()
        login_page.user_logout()
        login_page.check_user_is_not_authorization()
        login_page.favorite_is_empty_from_login_page_logout()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.favorites_is_empty()

    def test_add_two_products_to_favorite_auth_user(self, product_page_url, login_page_url, favorite_page_url, product_page_url_2):
        product_page = ProductPage(self.browser, product_page_url)
        product_page.favorite_is_empty()
        product_page.add_favorite_product()
        product_page.in_favorite_list_one_product()

        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_form_authorization()
        login_page.enter_user_data_for_authorization()
        login_page.check_user_is_authorization()
        login_page.check_product_in_favorite_from_login_page()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_one_product_in_favorites()

        product_page_2 = ProductPage(self.browser, product_page_url_2)
        product_page_2.in_favorite_list_one_product()
        product_page_2.add_favorite_product()
        product_page_2.in_favorite_list_two_products()

        favorite_page = FavoritePage(self.browser, favorite_page_url)
        favorite_page.check_two_products_in_favorites()

        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_user_cabinet()
        login_page.check_two_products_in_favorite_from_login_page()
        login_page.user_logout()
        login_page.check_user_is_not_authorization()
        login_page.favorite_is_empty_from_login_page_logout()
