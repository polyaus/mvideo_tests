import os

from pyvirtualdisplay import Display

from pages.mainpage import MainPage
from utils.browsers import build_browser
from utils.pages import main_page_close_ad


class TestsFromMainPage:
    @classmethod
    def setup_class(cls):
        if os.getenv("in_ci", False):
            cls.display = Display(visible=0, size=(1920, 1080))
            cls.display.start()

        cls.browser = build_browser()
        main_page_close_ad(cls.browser)

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

        if os.getenv("in_ci", False):
            cls.display.stop()

    def test_change_location_on_main_page(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.close_check_balans()
        main_page.change_location_to_kaliningrad()
        main_page.check_location_is_kaliningrad()

    def test_favorites_is_empty(self, main_page_url):
        main_page = MainPage(self.browser, main_page_url)
        main_page.favorites_is_empty()
