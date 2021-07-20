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

    def check_product_in_favorite_list(self):
        time.sleep(5)
        fav_product_icon = self.browser.find_element(*ProductPageLocators.OPEN_FAV_PRODUCTS)
        fav_product_icon.click()
        name_product_in_fav = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_FAV)
        assert name_product_in_fav.text == "Смартфон Apple iPhone 12 Pro Max 512GB Gold (MGDK3RU/A)", \
            "Your product is not favorite list"

    def delete_product_from_favorite_list(self):
        time.sleep(5)
        fav_product_icon = self.browser.find_element(*ProductPageLocators.OPEN_FAV_PRODUCTS)
        fav_product_icon.click()
        delete_product_from_favorite_list_from_fav_product_button = self.browser.find_element(*ProductPageLocators.delete_product_from_favorite_list_FROM_FAV_PRODUCT)
        delete_product_from_favorite_list_from_fav_product_button.click()

    def check_delete_product_from_favorite_list(self):
        text_after_delete = self.browser.find_element(*ProductPageLocators.TEXT_AFTER_DELETE)
        assert text_after_delete.text == "Все товары были убраны из вашего списка «Избранное»", \
            "Your product is favorite"
