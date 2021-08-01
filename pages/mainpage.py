import time

from pages.locators import MainPageLocators


class MainPage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

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
