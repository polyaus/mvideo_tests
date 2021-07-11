from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATION = (By.CSS_SELECTOR, ".header_fixed .header-top-line__link-text")
    CITY_INPUT = (By.CSS_SELECTOR, "#region-selection-form-city-input")
    GIVEN_CITY = (By.CSS_SELECTOR, ".city-selection-popup-results a")


class AuthorizationPageLocators:
    LOGIN = (By.CSS_SELECTOR, ".header-main .i-icon-fl-profile")
    TELEPHONE = (By.CSS_SELECTOR, "#login-original")
    PASSWORD = (By.CSS_SELECTOR, "#login_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    CABINET_HEAD = (By.CSS_SELECTOR, ".main-holder h1")
