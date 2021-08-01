import time

from pages.locators import ProductPageLocators
from pages.mainpage import MainPage


class ProductPage(MainPage):
    def add_favorite_product(self):
        icon_add_to_favorite = self.browser.find_element(*ProductPageLocators.ICON_ADD_TO_FAVORITE)
        icon_add_to_favorite.click()

    def in_favorite_list_one_product(self):
        time.sleep(5)
        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert int(favorite_icon.text) == 1, "Product is not added in favorite list"

    def favorite_is_empty(self):
        favorite_icon = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON)
        assert favorite_icon.text == '', "Favorite list is not empty"

    def favorite_list_is_not_empty(self):
        time.sleep(5)
        fav_product_icon = self.browser.find_element(*ProductPageLocators.OPEN_FAV_PRODUCTS)
        fav_product_icon.click()
        title_selected = self.browser.find_element(*ProductPageLocators.TITLE_SELECTED)
        assert title_selected.text == "Избранное", "Favorite list is empty"

    def open_favorite_list(self):
        time.sleep(5)
        fav_product_icon = self.browser.find_element(*ProductPageLocators.OPEN_FAV_PRODUCTS)
        fav_product_icon.click()

    def check_product_in_favorite_list(self):
        time.sleep(5)
        name_product_in_fav = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_FAV)
        assert name_product_in_fav.text == "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)", \
            "Product is not favorite list"
        count_fav_products = self.browser.find_element(*ProductPageLocators.COUNT_PRODUCTS_IN_FAV)
        assert int(count_fav_products.text) == 1, "Favorite list has more one product"

    def check_two_products_in_favorite_list(self):
        count_fav_products = self.browser.find_element(*ProductPageLocators.COUNT_PRODUCTS_IN_FAV)
        assert int(count_fav_products.text) == 2, "Favorite list has more one product"
        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        fav_list_items = self.browser.find_elements(*ProductPageLocators.NAME_PRODUCT_IN_FAV)
        assert len(fav_list_items) == 2, "Favorite list has items not equals 2"
        assert fav_list_items[0].text == product_names[0], "Wrong favorite product name"
        assert fav_list_items[1].text == product_names[1], "Wrong favorite product name"

    def delete_product_from_favorite_list(self):
        delete_fav_product_button = self.browser.find_element(*ProductPageLocators.DELETE_FROM_FAV_PRODUCT)
        delete_fav_product_button.click()

    def delete_first_added_product_from_favorite_list(self):
        time.sleep(5)
        product_names = [
            "Смартфон Xiaomi Redmi 9A 32GB Peacock Green",
            "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)",
        ]
        delete_fav_product_buttons = self.browser.find_elements(*ProductPageLocators.DELETE_FROM_FAV_PRODUCT)
        delete_fav_product_buttons[1].click()
        fav_list_items = self.browser.find_elements(*ProductPageLocators.NAME_PRODUCT_IN_FAV)
        assert len(fav_list_items) == 1, "Favorite list has items not equals 2"
        assert fav_list_items[0].text == product_names[0], "Wrong favorite product name"
