from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def open_authorization_form(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_WITH_PASSWORD))

        login_with_password = self.browser.find_element(*LoginPageLocators.LOGIN_WITH_PASSWORD)
        if login_with_password.text == "Войти с помощью пароля":
            login_with_password.click()

    def enter_user_data_in_authorization_form(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.PASSWORD))

        telephone = self.browser.find_element(*LoginPageLocators.TELEPHONE)
        telephone.send_keys("79220344446")

        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("1232345Arc")

        enter_btn = self.browser.find_element(*LoginPageLocators.ENTER_BTN)
        enter_btn.click()

    def open_user_cabinet(self):
        user_cabinet = self.browser.find_element(*LoginPageLocators.LOGIN)
        user_cabinet.click()

    def check_user_is_logged(self):
        cabinet_head = self.browser.find_element(*LoginPageLocators.CABINET_HEAD)
        assert cabinet_head.text == "Личный кабинет", f"User is not logged, {cabinet_head.text}"

    def user_logout(self):
        try:
            self.check_user_is_logged()
        except NoSuchElementException:
            return

        user_cabinet = self.browser.find_element(*LoginPageLocators.LOGIN)
        action = ActionChains(self.browser)
        action.move_to_element(user_cabinet).perform()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGOUT))

        logout_btn = self.browser.find_element(*LoginPageLocators.LOGOUT)
        logout_btn.click()

    def check_user_is_not_logged(self):
        user_cabinet = self.browser.find_elements(*LoginPageLocators.USER_ENTER)
        assert user_cabinet[1].text == "Войти", f"User is in login cabinet, {user_cabinet[1].text}"

    def favorites_is_empty_user_logged(self):
        favorites_header = self.browser.find_element(*LoginPageLocators.FAVORITES_HEADER)
        assert favorites_header.text == '', f"Favorites is not empty, {favorites_header.text}"

        favorites_footer = self.browser.find_element(*LoginPageLocators.FAVORITES_FOOTER)
        assert int(favorites_footer.text) == 0, f"Favorites is not empty, {favorites_footer.text}"

    def check_one_product_in_favorites_user_logged(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.FAVORITES_FOOTER))

        favorites_header = self.browser.find_element(*LoginPageLocators.FAVORITES_HEADER)
        assert int(favorites_header.text) == 1, f"Favorites has no one product, {favorites_header.text}"

        favorites_footer = self.browser.find_element(*LoginPageLocators.FAVORITES_FOOTER)
        assert int(favorites_footer.text) == 1, f"Favorites has no one product, {favorites_footer.text}"

    def check_two_products_in_favorites_user_logged(self):
        favorites_header = self.browser.find_element(*LoginPageLocators.FAVORITES_HEADER)
        assert int(favorites_header.text) == 2, f"Favorites has no two products, {favorites_header.text}"

        favorites_footer = self.browser.find_element(*LoginPageLocators.FAVORITES_FOOTER)
        assert int(favorites_footer.text) == 2, f"Favorites has no two products, {favorites_footer.text}"

    def favorites_is_empty_user_logout(self):
        favorites_header = self.browser.find_element(*LoginPageLocators.EMPTY_FAVORITES_HEADER)
        assert favorites_header, f"Favorite list is not empty, {favorites_header.text}"
