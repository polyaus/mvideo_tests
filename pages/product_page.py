from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_favorite_product(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.ICON_ADD_TO_FAVORITE))

        icon_add_to_favorite = self.browser.find_element(*ProductPageLocators.ICON_ADD_TO_FAVORITE)
        icon_add_to_favorite.click()

    def add_favorite_product_authorizated_user(self):
        icon_add_to_favorite = self.browser.find_element(*ProductPageLocators.ICON_ADD_TO_FAVORITE_AUTH_USER)
        icon_add_to_favorite.click()

    def del_favorite_product(self):
        body = self.browser.find_element(*ProductPageLocators.BODY)
        action = ActionChains(self.browser)
        action.move_to_element(body).perform()
        body.click()

        self.add_favorite_product()

    def favorite_is_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.FAVORITE_ICON), "Favorite list is not empty"

    def in_favorite_list_one_product(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON))

        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert int(favorite_icon.text) == 1, f"Product is not added in favorite list, {favorite_icon.text}"

    def in_favorite_list_one_product_authorizated_user(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until_not(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON))

        favorite_icon = self.browser.find_element(*ProductPageLocators.AMOUNT_WISHLIST)
        assert int(favorite_icon.text) == 1, f"Product is not added in favorite list, {favorite_icon.text}"

    def in_favorite_list_two_products(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until_not(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON_ANIMATED))

        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert int(favorite_icon.text) == 2, f"Product is not added in favorite list, {favorite_icon.text}"

    def close_ad(self):
        try:
            element = self.browser.find_element(*ProductPageLocators.CLOSE_AD)
        except NoSuchElementException:
            return

        element.click()
