from pages.mainpage import MainPage
from utils.browsers import build_browser
from utils.pages import main_page_close_ad


class TestsFromMainPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()
        main_page_close_ad(cls.browser)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_change_location_on_main_page(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.change_location_to_kaliningrad()
        main_page.check_location_is_kaliningrad()

    def test_favorite_list_is_empty(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.favorite_list_is_empty()
