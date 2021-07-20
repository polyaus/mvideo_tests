from pages.product_page import ProductPage


def test_add_product_to_fav(browser, product_page_url):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_favorite_product()
    page.in_favorite_list_one_product()
    page.check_product_in_favorite_list()


def test_favorite_list_is_empty(browser, product_page_url):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.favorite_is_empty()


def test_favorite_list_is_not_empty(browser, product_page_url):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.favorite_is_empty()
    page.add_favorite_product()
    page.favorite_list_is_not_empty()


def test_product_in_favorite_list(browser, product_page_url):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_favorite_product()
    page.check_product_in_favorite_list()


# def test_add_two_product_in_fav(browser, product_page_url, product_page_url_2):
#     page = ProductPage(browser, product_page_url)
#     page.open()
#     page.add_favorite_product()
#     page_2 = ProductPage(browser, product_page_url_2)
#     page_2.open()
#     page_2.add_favorite_product()
#     time.sleep(15)
#
# def test_add_product_to_fav_for_login_user(browser, main_page_url, product_page_url):
#     page = LoginPage(browser, main_page_url)
#     page.open()
#     page.user_authorization()
#     product_page = ProductPage(browser, product_page_url)
#     product_page.open()
#     product_page.add_favorite_product()
#     product_page.check_product_is_favorite()
#
#
# def test_delete_product_from_favorite_list(browser, product_page_url):
#     page = ProductPage(browser, product_page_url)
#     page.open()
#     page.add_favorite_product()
#     page.delete_product_from_favorite_list()
