from pages.mainpage import MainPage
from utils.browsers import build_browser


class TestsFromMainPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_change_location_on_main_page(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.click_body()
        main_page.change_location_to_kaliningrad()
        main_page.check_location_is_kaliningrad()

    def test_favorite_list_is_empty(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.open_favorite_list_from_main_page()
        main_page.favorite_list_is_empty()
