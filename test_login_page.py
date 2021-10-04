from conftest import LOGIN_PAGE_URL
from pages.login_page import LoginPage
from utils.browsers import build_browser


class TestsFromLoginPage:
    @classmethod
    def setup_class(cls):
        cls.browser = build_browser()

    @classmethod
    def teardown_class(cls):
        cls.browser.quit()

    def test_user_auth(self):
        login_page = LoginPage(self.browser, LOGIN_PAGE_URL)
        login_page.open_form_authorization()
        login_page.enter_user_data_for_authorization()
        login_page.open_user_cabinet()
        login_page.check_user_is_authorization()
