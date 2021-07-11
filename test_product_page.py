from pages.product_page import ProductPage


def test_add_product_to_fav(browser, product_page_url):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_favorite_product()
    page.check_product_is_favorite()
