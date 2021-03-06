from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import FavoritePageLocators


class FavoritePage(BasePage):
    def favorites_is_empty(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.EMPTY_FAVORITES))

        empty_favorites = self.browser.find_element(*FavoritePageLocators.EMPTY_FAVORITES)
        assert empty_favorites.text == 'В избранном пока ничего нет', \
            f"Favorites is not empty, {empty_favorites.text}"

    def favorites_is_not_empty(self):
        favorites = self.browser.find_element(*FavoritePageLocators.FAVORITES)
        assert favorites.text == 'Избранное', f"Favorites is empty, {favorites.text}"

    def check_one_product_in_favorites(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.NAME_PRODUCT))

        name_product = self.browser.find_element(*FavoritePageLocators.NAME_PRODUCT)
        assert name_product.text == 'Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)', \
            f"Product is not in favorites, {name_product.text}"

        favorites_count = self.browser.find_element(*FavoritePageLocators.COUNT_IN_FAVORITES)
        assert int(favorites_count.text) == 1, \
            f"Favorites has more or less one product, {favorites_count.text}"

    def check_two_products_in_favorites(self):
        favorites_count = self.browser.find_element(*FavoritePageLocators.COUNT_IN_FAVORITES)
        assert int(favorites_count.text) == 2, \
            f"Favorites has more or less one product, {favorites_count.text}"

        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        favorite_products = self.browser.find_elements(*FavoritePageLocators.NAME_PRODUCT)
        assert len(favorite_products) == 2, f"Favorites has products not equal 2, {len(favorite_products)}"
        assert favorite_products[0].text != favorite_products[1].text, \
            f"Duplicate product names, {favorite_products[0].text}"
        assert favorite_products[0].text in product_names, \
            f"Wrong favorite product name, {favorite_products[0].text}"
        assert favorite_products[1].text in product_names, \
            f"Wrong favorite product name, {favorite_products[1].text}"

    def delete_one_product_from_favorites(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.DELETE_FAVORITES_BTN))

        delete_favorites_button = self.browser.find_element(*FavoritePageLocators.DELETE_FAVORITES_BTN)
        delete_favorites_button.click()

    def delete_all_products_from_favorites(self):
        try:
            wait = WebDriverWait(self.browser, 5)
            wait.until(EC.presence_of_element_located(FavoritePageLocators.DELETE_FAVORITES_BTN))
        except TimeoutException:
            return

        for _ in range(50):
            delete_favorites_buttons = self.browser.find_elements(*FavoritePageLocators.DELETE_FAVORITES_BTN)
            if not delete_favorites_buttons:
                break
            delete_favorites_buttons[0].click()

    def delete_first_added_product_in_favorites(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.DELETE_FAVORITES_BTN))

        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        delete_favorites_buttons = self.browser.find_elements(*FavoritePageLocators.DELETE_FAVORITES_BTN)
        assert len(delete_favorites_buttons) == 2, \
            f"Delete favorites buttons sum are not two, {len(delete_favorites_buttons)}"
        delete_favorites_buttons[1].click()

        favorites = self.browser.find_elements(*FavoritePageLocators.NAME_PRODUCT)
        assert len(favorites) == 1, f"Favorites sum is not equals 2, {len(favorites)}"
        assert favorites[0].text == product_names[0], f"Wrong favorite product name, {favorites[0].text}"

    def favorites_is_empty_after_delete_products(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.EMPTY_FAVORITES_AFTER_DELETE))

        empty_favorites = self.browser.find_element(*FavoritePageLocators.EMPTY_FAVORITES_AFTER_DELETE)
        assert empty_favorites.text == 'Все товары были убраны из вашего списка «Избранное»', \
            f"Favorites is not empty, {empty_favorites.text}"
