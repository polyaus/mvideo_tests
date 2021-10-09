from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_favorites(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_ADD_TO_FAVORITES))

        add_to_favorites = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_FAVORITES)
        add_to_favorites.click()

    def del_product_from_favorites(self):
        body = self.browser.find_element(*ProductPageLocators.BODY)
        action = ActionChains(self.browser)
        action.move_to_element(body).perform()
        body.click()

        try:
            self.browser.find_element(*ProductPageLocators.ACTIVE_BTN_ADD_TO_FAVORITES)
        except NoSuchElementException:
            return
        else:
            self.add_product_to_favorites()

    def favorites_is_empty(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.EMPTY_FAVORITES))

        assert self.is_not_element_present(*ProductPageLocators.FAVORITES_ICON_TOP), "Favorites is not empty"

    def one_product_in_favorites(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.FAVORITES_ICON_TOP))

        favorites_icon_top = self.browser.find_element(*ProductPageLocators.FAVORITES_ICON_TOP)
        assert int(favorites_icon_top.text) == 1, f"Favorites has less or more one product, {favorites_icon_top.text}"

    def two_products_in_favorites(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until_not(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON_ANIMATED))

        favorite_icon_top = self.browser.find_element(*ProductPageLocators.FAVORITES_ICON_TOP)
        assert int(favorite_icon_top.text) == 2, f"Favorites has less or more two product, {favorite_icon_top.text}"
