from pages.mainpage import MainPage


def test_change_location_on_main_page(browser, main_page_url):
    page = MainPage(browser, main_page_url)
    page.open()
    page.change_location_to_kaliningrad()
    page.check_location_is_kaliningrad()
