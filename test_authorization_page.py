from pages.login_page import LoginPage


def test_user_auth(browser, main_page_url):
    page = LoginPage(browser, main_page_url)
    page.open()
    page.user_authorization()
    page.enter_login_cabinet()
    page.check_user_is_authorization()
