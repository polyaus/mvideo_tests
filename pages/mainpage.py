from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def change_location_to_kaliningrad(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.LOCATION))

        locate = self.browser.find_element(*MainPageLocators.LOCATION)
        locate.click()

        input_city = self.browser.find_element(*MainPageLocators.INPUT_CITY)
        input_city.send_keys("Калининград")

        for _ in range(100):
            list_cities = self.browser.find_elements(*MainPageLocators.LIST_CITIES)
            if len(list_cities) == 2:
                break

        for city in list_cities:
            if city.text == "г Калининград":
                city.click()
                break

    def check_location_is_kaliningrad(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.text_to_be_present_in_element(MainPageLocators.LOCATION, "Калининград"))

        actual_city = self.browser.find_element(*MainPageLocators.LOCATION)
        assert actual_city.text == "Калининград", f"City is not corrected, {actual_city.text}"

    def favorites_is_empty(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until_not(EC.presence_of_element_located(MainPageLocators.FAVORITES_ICON))
