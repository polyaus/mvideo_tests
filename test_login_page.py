from conftest import LOGIN_PAGE_URL
from pages.login_page import LoginPage


def test_user_auth(browser):
    login_page = LoginPage(browser, LOGIN_PAGE_URL)
    login_page.open_form_authorization()
    login_page.enter_user_data_for_authorization()
    login_page.open_user_cabinet()
    login_page.check_user_is_authorization()
