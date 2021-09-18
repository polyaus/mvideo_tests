import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.locators import FavoritePageLocators


class FavoritePage(BasePage):
    def open(self):
        time.sleep(2)
        super().open()

    def favorite_list_is_empty_from_favorite_list(self):
        text_empty_favorite_list = self.browser.find_element(*FavoritePageLocators.TEXT_EMPTY_FAVORITE_LIST)
        assert text_empty_favorite_list.text == 'В избранном пока ничего нет', \
            f"Favorite list is empty, {text_empty_favorite_list.text}"

    def favorite_list_is_not_empty(self):
        title_selected = self.browser.find_element(*FavoritePageLocators.TITLE_SELECTED)
        assert title_selected.text == 'Избранное', f"Favorite list is empty, {title_selected.text}"

    def check_product_in_favorite_list(self):
        name_product_in_fav = self.browser.find_element(*FavoritePageLocators.NAME_PRODUCT_IN_FAV)
        assert name_product_in_fav.text == 'Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)', \
            f"Product is not favorite list, {name_product_in_fav.text}"

        count_fav_products = self.browser.find_element(*FavoritePageLocators.COUNT_PRODUCTS_IN_FAV)
        assert int(count_fav_products.text) == 1, f"Favorite list has more one product, {count_fav_products.text}"

    def check_two_products_in_favorite_list(self):
        count_fav_products = self.browser.find_element(*FavoritePageLocators.COUNT_PRODUCTS_IN_FAV)
        assert int(count_fav_products.text) == 2, f"Favorite list has more one product, {count_fav_products.text}"

        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        fav_list_items = self.browser.find_elements(*FavoritePageLocators.NAME_PRODUCT_IN_FAV)
        assert len(fav_list_items) == 2, f"Favorite list has items not equals 2, {len(fav_list_items)}"
        assert fav_list_items[0].text != fav_list_items[1].text, f"Duplicate product names, {fav_list_items[0].text}"
        assert fav_list_items[0].text in product_names, f"Wrong favorite product name, {fav_list_items[0].text}"
        assert fav_list_items[1].text in product_names, f"Wrong favorite product name, {fav_list_items[1].text}"

    def delete_product_from_favorite_list(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.DELETE_FROM_FAV_PRODUCT))

        delete_fav_product_button = self.browser.find_element(*FavoritePageLocators.DELETE_FROM_FAV_PRODUCT)
        delete_fav_product_button.click()

    def delete_first_added_product_from_favorite_list(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.DELETE_FROM_FAV_PRODUCT))

        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        delete_fav_product_buttons = self.browser.find_elements(*FavoritePageLocators.DELETE_FROM_FAV_PRODUCT)
        assert len(delete_fav_product_buttons) == 2, \
            f"Delete favorite products buttons count is not two, {len(delete_fav_product_buttons)}"
        delete_fav_product_buttons[1].click()

        fav_list_items = self.browser.find_elements(*FavoritePageLocators.NAME_PRODUCT_IN_FAV)
        assert len(fav_list_items) == 1, f"Favorite list has items not equals 2, {len(fav_list_items)}"
        assert fav_list_items[0].text == product_names[0], f"Wrong favorite product name, {fav_list_items[0].text}"

    def favorite_list_is_empty_after_delete_product(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(FavoritePageLocators.TEXT_AFTER_DELETE))

        text_empty_favorite_list = self.browser.find_element(*FavoritePageLocators.TEXT_AFTER_DELETE)
        assert text_empty_favorite_list.text == 'Все товары были убраны из вашего списка «Избранное»', \
            f"Favorite list is empty, {text_empty_favorite_list.text}"
