from pages.locators import ProductPageLocators
from pages.mainpage import MainPage


class ProductPage(MainPage):
    def add_favorite_product(self):
        icon_favorite = self.browser.find_element(*ProductPageLocators.ICON_FAVORITE)
        icon_favorite.click()

    def check_product_is_favorite(self):
        fav_product_icon = self.browser.find_element(*ProductPageLocators.OPEN_FAV_PRODUCTS)
        fav_product_icon.click()
