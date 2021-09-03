from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def user_authorization(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN)
        login_button.click()

        self.browser.execute_script(f"$({LoginPageLocators.ENTER_WITH_PASSWORD_BUTTON}).click()")

        telephone_field = self.browser.find_element(*LoginPageLocators.TELEPHONE)
        telephone_field.send_keys("79220344446")

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys("1232345Arc")

        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def user_login(self):
        user_login = self.browser.find_element(*LoginPageLocators.LOGIN)
        user_login.click()

    def check_user_is_authorization(self):
        cabinet_head = self.browser.find_element(*LoginPageLocators.CABINET_HEAD)
        assert cabinet_head.text == "Личный кабинет", f"User is not authorized, {cabinet_head.text}"

    def user_logout(self):
        user_logout_menu = self.browser.find_element(*LoginPageLocators.LOGIN)
        action = ActionChains(self.browser)
        action.move_to_element(user_logout_menu).perform()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGOUT))

        user_logout = self.browser.find_element(*LoginPageLocators.LOGOUT)
        user_logout.click()

    def check_user_is_not_authorization(self):
        text_on_button_enter = self.browser.find_elements(*LoginPageLocators.TEXT_ON_BUTTON_ENTER)
        assert text_on_button_enter[1].text == "Войти", f"User is in login cabinet, {text_on_button_enter[1].text}"
