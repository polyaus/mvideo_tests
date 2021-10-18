import os

from pyvirtualdisplay import Display

from pages.login_page import LoginPage
from utils.browsers import build_browser


class TestsFromLoginPage:
    @classmethod
    def setup_class(cls):
        if os.getenv("in_ci", False):
            cls.display = Display(visible=0, size=(1920, 1080))
            cls.display.start()

        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

        if os.getenv("in_ci", False):
            cls.display.stop()

    def test_user_logged(self, login_page_url):
        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_authorization_form()
        login_page.enter_user_data_in_authorization_form()
        login_page.open_user_cabinet()
        login_page.check_user_is_logged()
