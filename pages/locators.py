from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATION = (By.CSS_SELECTOR, ".header_fixed .header-top-line__link-text")
    CITY_INPUT = (By.CSS_SELECTOR, "#region-selection-form-city-input")
    GIVEN_CITY = (By.CSS_SELECTOR, ".city-selection-popup-results a")
    CLOSE_AD = (By.CSS_SELECTOR, ".flocktory-widget-overlay")


class AuthorizationPageLocators:
    LOGIN = (By.CSS_SELECTOR, ".header-main .i-icon-fl-profile")
    TELEPHONE = (By.CSS_SELECTOR, "#login-original")
    PASSWORD = (By.CSS_SELECTOR, "#login_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    CABINET_HEAD = (By.CSS_SELECTOR, ".main-holder h1")


class ProductPageLocators:
    ICON_ADD_TO_FAVORITE = (By.CSS_SELECTOR, ".c-checkbox .i-icon-fl-favorite .c-btn__text")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".header-icon__icon .wishlist-amount")
    OPEN_FAV_PRODUCTS = (By.CSS_SELECTOR, ".header-icon .i-icon-fl-favorite")
    TITLE_SELECTED = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-title")
    NAME_PRODUCT_IN_FAV = (By.CSS_SELECTOR, ".wishlist-items-container .wishlist-item .wishlist-product-title a")
    COUNT_PRODUCTS_IN_FAV = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-quantity")
    DELETE_FROM_FAV_PRODUCT = (By.CSS_SELECTOR, "#wishlist-action-area-0 .wishlist-action-links .wishlist-ico-action")
    TEXT_AFTER_DELETE = (By.CSS_SELECTOR, ".c-notifications .c-notifications__messages")
