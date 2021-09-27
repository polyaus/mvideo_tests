from pages.favorite_page import FavoritePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_favorite_list_is_empty_from_favorite_list(browser, favorite_page_url):
    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.favorite_list_is_empty_from_favorite_list()


def test_add_product_to_fav(browser, product_page_url, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()


def test_favorite_list_is_not_empty(browser, product_page_url, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.favorite_list_is_not_empty()


def test_delete_product_from_favorite_list(browser, product_page_url, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()
    favorite_page.delete_product_from_favorite_list()
    favorite_page.favorite_list_is_empty_after_delete_product()


def test_add_two_product_in_favorite_list(browser, product_page_url, product_page_url_2, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    product_page_2 = ProductPage(browser, product_page_url_2)
    product_page_2.add_favorite_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_two_products_in_favorite_list()


def test_delete_first_added_product_from_favorite_list(browser, product_page_url, product_page_url_2, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    product_page_2 = ProductPage(browser, product_page_url_2)
    product_page_2.add_favorite_product()
    product_page_2.in_favorite_list_two_products()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_first_added_product_from_favorite_list()


def test_delete_all_two_products_from_favorite_list(browser, product_page_url, product_page_url_2, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    product_page_2 = ProductPage(browser, product_page_url_2)
    product_page_2.add_favorite_product()
    product_page_2.in_favorite_list_two_products()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_two_products_in_favorite_list()
    favorite_page.delete_all_products_from_favorite_list()
    favorite_page.favorite_list_is_empty_after_delete_product()


def test_authorization_after_add_one_product_in_favorite_list(browser, product_page_url, login_page_url, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_form_authorization()
    login_page.enter_user_data_for_authorization()
    login_page.open_user_cabinet_after_add_to_favorite_product()
    login_page.check_user_is_authorization()
    login_page.check_product_in_favorite_from_login_page()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_user_cabinet()
    login_page.user_logout()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.enter_user_data_for_authorization()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()


def test_add_product_to_favorite_is_not_visible_outside(browser, login_page_url, product_page_url, favorite_page_url):
    login_page = LoginPage(browser, login_page_url)
    login_page.open_form_authorization()
    login_page.enter_user_data_for_authorization()
    login_page.open_user_cabinet()
    login_page.check_user_is_authorization()
    login_page.favorite_is_empty_from_login_page()

    product_page = ProductPage(browser, product_page_url)
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_user_cabinet()
    login_page.check_product_in_favorite_from_login_page()
    login_page.user_logout()
    login_page.check_user_is_not_authorization()
    login_page.favorite_is_empty_from_login_page_logout()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.favorite_list_is_empty_from_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_user_cabinet()
    login_page.user_logout()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.enter_user_data_for_authorization()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()


def test_add_two_products_to_favorite_auth_user(browser, login_page_url, product_page_url, product_page_url_2, favorite_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.close_ad()
    product_page.favorite_is_empty()
    product_page.add_favorite_product()
    product_page.in_favorite_list_one_product()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_form_authorization()
    login_page.enter_user_data_for_authorization()
    login_page.open_user_cabinet_after_add_to_favorite_product()
    login_page.check_user_is_authorization()
    login_page.check_product_in_favorite_from_login_page()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_product_in_favorite_list()

    product_page_2 = ProductPage(browser, product_page_url_2)
    product_page_2.in_favorite_list_one_product()
    product_page_2.add_favorite_product()
    product_page_2.in_favorite_list_two_products()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.check_two_products_in_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_user_cabinet()
    login_page.check_two_products_in_favorite_from_login_page()
    login_page.user_logout()
    login_page.favorite_is_empty_from_login_page_logout()

    login_page = LoginPage(browser, login_page_url)
    login_page.open_user_cabinet()
    login_page.user_logout()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()

    login_page = LoginPage(browser, login_page_url)
    login_page.enter_user_data_for_authorization()

    favorite_page = FavoritePage(browser, favorite_page_url)
    favorite_page.delete_all_products_from_favorite_list()
