from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_favorite_product(self):
        icon_add_to_favorite = self.browser.find_element(*ProductPageLocators.ICON_ADD_TO_FAVORITE)
        icon_add_to_favorite.click()

    def favorite_is_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.FAVORITE_ICON), "Favorite list is not empty"

    def in_favorite_list_one_product(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON))

        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert int(favorite_icon.text) == 1, "Product is not added in favorite list"

    def in_favorite_list_two_products(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(ProductPageLocators.FAVORITE_ICON))

        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert int(favorite_icon.text) == 2, "Product is not added in favorite list"

    def close_ad(self):
        element = self.browser.find_element(*ProductPageLocators.CLOSE_AD)
        element.click()
