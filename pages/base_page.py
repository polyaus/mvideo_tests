import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

        self.setup_browser(timeout)
        self.open()

    def setup_browser(self, timeout):
        self.browser.implicitly_wait(timeout)

    def open(self):
        time.sleep(2)
        self.browser.get(self.url)

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

    def click_body(self):
        body = self.browser.find_element(*BasePageLocators.BODY)
        action = ActionChains(self.browser)
        action.move_to_element(body).perform()
        body.click()

    def close_ad(self):
        try:
            element = self.browser.find_element(*BasePageLocators.CLOSE_AD)
        except NoSuchElementException:
            return

        element.click()
