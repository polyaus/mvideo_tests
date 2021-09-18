from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def open_form_authorization(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN))

        login_button = self.browser.find_element(*LoginPageLocators.LOGIN)
        login_button.click()

        self.browser.execute_script(f"$({LoginPageLocators.ENTER_WITH_PASSWORD_BUTTON}).click()")

    def enter_user_data_for_authorization(self):
        telephone_field = self.browser.find_element(*LoginPageLocators.TELEPHONE)
        telephone_field.send_keys("79220344446")

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys("1232345Arc")

        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def open_user_cabinet(self):
        enter_login_cabinet = self.browser.find_element(*LoginPageLocators.LOGIN)
        enter_login_cabinet.click()

    def open_user_cabinet_after_add_to_favorite_product(self):
        icon_login_cabinet = self.browser.find_element(*LoginPageLocators.USER)
        action = ActionChains(self.browser)
        action.move_to_element(icon_login_cabinet).perform()
        # icon_login_cabinet.click()

        enter_login_cabinet = self.browser.find_element(*LoginPageLocators.USERNAME)
        action = ActionChains(self.browser)
        action.move_to_element(enter_login_cabinet).perform()
        enter_login_cabinet.click()

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

    def favorite_is_empty_from_login_page(self):
        count_fav_products_up = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_UP)
        assert count_fav_products_up.text == '', f"Favorite list is not empty, {count_fav_products_up.text}"

        count_fav_products_down = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_DOWN)
        assert int(count_fav_products_down.text) == 0, f"Favorite list is not empty, {count_fav_products_down.text}"

    def check_product_in_favorite_from_login_page(self):
        count_fav_products_up = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_UP)
        assert int(count_fav_products_up.text) == 1, f"Favorite list has no one product, {count_fav_products_up.text}"

        count_fav_products_down = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_DOWN)
        assert int(count_fav_products_down.text) == 1, \
            f"Favorite list has no one product, {count_fav_products_down.text}"

    def check_two_products_in_favorite_from_login_page(self):
        count_fav_products_up = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_UP)
        assert int(count_fav_products_up.text) == 2, f"Favorite list has no one product, {count_fav_products_up.text}"

        count_fav_products_down = self.browser.find_element(*LoginPageLocators.COUNT_PROD_IN_FAV_FROM_LP_DOWN)
        assert int(count_fav_products_down.text) == 2, \
            f"Favorite list has no one product, {count_fav_products_down.text}"

    def favorite_is_empty_from_login_page_logout(self):
        # wait = WebDriverWait(self.browser, 10)
        # wait.until_not(EC.presence_of_element_located(LoginPageLocators.EMPTY_WISH_LIST))
        # time.sleep(5)

        count_fav_products_up = self.browser.find_element(*LoginPageLocators.EMPTY_WISH_LIST)
        assert count_fav_products_up, f"Favorite list is not empty, {count_fav_products_up.text}"
