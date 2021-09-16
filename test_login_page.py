from pages.login_page import LoginPage


def test_user_auth(browser, login_page_url):
    login_page = LoginPage(browser, login_page_url)
    login_page.user_authorization()
    login_page.open_user_cabinet()
    login_page.check_user_is_authorization()
