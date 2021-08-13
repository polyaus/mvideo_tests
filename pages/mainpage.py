from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open_favorite_list_from_main_page(self):
        self.browser.execute_script("$('.header-icon__icon .i-icon-fl-favorite').click()")

    def favorite_list_is_empty(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.TEXT_EMPTY_FAV_LIST))
        text_in_empty_favorite_list = self.browser.find_element(*MainPageLocators.TEXT_EMPTY_FAV_LIST)
        assert text_in_empty_favorite_list.text == 'В избранном пока ничего нет', "Favorite list is not empty!"
        amount_favorite_on_button = self.browser.find_element(*MainPageLocators.AMOUNT_WISHLIST)
        assert amount_favorite_on_button.text == '', "Favorite list is not empty, sorry"
