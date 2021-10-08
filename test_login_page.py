from pages.login_page import LoginPage
from utils.browsers import build_browser


class TestsFromLoginPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_user_auth(self, login_page_url):
        login_page = LoginPage(self.browser, login_page_url)
        login_page.open_authorization_form()
        login_page.enter_user_data_in_authorization_form()
        login_page.open_user_cabinet()
        login_page.check_user_is_logged()
