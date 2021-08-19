from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def change_location_to_kaliningrad(self):
        locate = self.browser.find_element(*MainPageLocators.LOCATION)
        locate.click()

        entry_field = self.browser.find_element(*MainPageLocators.CITY_INPUT)
        entry_field.send_keys("Калининград")

        given_cities = self.browser.find_elements(*MainPageLocators.GIVEN_CITY)
        for given_city in given_cities:
            if given_city.text.startswith("Калининград,"):
                given_city.click()
                break

    def check_location_is_kaliningrad(self):
        actual_city = self.browser.find_element(*MainPageLocators.LOCATION)
        assert actual_city.text == "Калининград", "City is not corrected"

    def open_favorite_list_from_main_page(self):
        self.browser.execute_script(f"$({MainPageLocators.FAVORITE_ICON_BUTTON}).click()")

    def favorite_list_is_empty(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.TEXT_EMPTY_FAV_LIST))

        text_in_empty_favorite_list = self.browser.find_element(*MainPageLocators.TEXT_EMPTY_FAV_LIST)
        assert text_in_empty_favorite_list.text == 'В избранном пока ничего нет', "Favorite list is not empty!"

        amount_favorite_on_button = self.browser.find_element(*MainPageLocators.AMOUNT_WISHLIST)
        assert amount_favorite_on_button.text == '', "Favorite list is not empty, sorry"

    def close_ad_1(self):
        element = self.browser.find_element(*MainPageLocators.CLOSE_AD)
        element.click()
