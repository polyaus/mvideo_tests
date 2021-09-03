from pages.login_page import LoginPage


def test_user_auth(browser, login_page_url):
    login_page = LoginPage(browser, login_page_url)
    login_page.user_authorization()
    login_page.user_login()
    login_page.check_user_is_authorization()


def test_user_login_and_logout(browser, login_page_url):
    login_page = LoginPage(browser, login_page_url)
    login_page.user_authorization()
    login_page.user_login()
    login_page.check_user_is_authorization()
    login_page.user_logout()
    login_page.check_user_is_not_authorization()
