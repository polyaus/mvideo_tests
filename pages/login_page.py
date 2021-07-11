from pages.locators import AuthorizationPageLocators
from pages.mainpage import MainPage


class LoginPage(MainPage):
    def user_authorization(self):
        login_button = self.browser.find_element(*AuthorizationPageLocators.LOGIN)
        login_button.click()
        self.browser.execute_script("$('.o-login__login .c-link').click()")
        telephone_field = self.browser.find_element(*AuthorizationPageLocators.TELEPHONE)
        telephone_field.send_keys("79220344446")
        password_field = self.browser.find_element(*AuthorizationPageLocators.PASSWORD)
        password_field.send_keys("1232345Arc")
        submit_button = self.browser.find_element(*AuthorizationPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def enter_login_cabinet(self):
        enter_login_cabinet = self.browser.find_element(*AuthorizationPageLocators.LOGIN)
        enter_login_cabinet.click()

    def check_user_is_authorization(self):
        cabinet_head = self.browser.find_element(*AuthorizationPageLocators.CABINET_HEAD)
        assert cabinet_head.text == "Личный кабинет", "User is not authorized"
