from pages.locators import LoginPageLocators
from pages.mainpage import MainPage


class LoginPage(MainPage):
    def user_authorization(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN)
        login_button.click()
        self.browser.execute_script("$('.o-login__login .c-link').click()")
        telephone_field = self.browser.find_element(*LoginPageLocators.TELEPHONE)
        telephone_field.send_keys("79220344446")
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys("1232345Arc")
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def enter_login_cabinet(self):
        enter_login_cabinet = self.browser.find_element(*LoginPageLocators.LOGIN)
        enter_login_cabinet.click()

    def check_user_is_authorization(self):
        cabinet_head = self.browser.find_element(*LoginPageLocators.CABINET_HEAD)
        assert cabinet_head.text == "Личный кабинет", "User is not authorized"
