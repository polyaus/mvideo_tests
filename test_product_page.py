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
