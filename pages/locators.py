from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATION = (By.CSS_SELECTOR, ".header_fixed .header-top-line__link-text")
    CITY_INPUT = (By.CSS_SELECTOR, "#region-selection-form-city-input")
    GIVEN_CITY = (By.CSS_SELECTOR, ".city-selection-popup-results a")
    FAVORITE_ICON_BUTTON = (By.CSS_SELECTOR, ".header-icon__icon .i-icon-fl-favorite")
    TEXT_EMPTY_FAV_LIST = (By.CSS_SELECTOR, ".whishlist-empty .whishlist-empty__title")
    AMOUNT_WISHLIST = (By.CSS_SELECTOR, ".header-main__icon_wish .wishlist-amount")
    CLOSE_AD = (By.CSS_SELECTOR, ".c-popup.c-popup_facelift")


class LoginPageLocators:
    LOGIN = (By.CSS_SELECTOR, ".header-main .i-icon-fl-profile")
    ENTER_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".o-login__login .c-link")
    TELEPHONE = (By.CSS_SELECTOR, "#login-original")
    PASSWORD = (By.CSS_SELECTOR, "#login_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    CABINET_HEAD = (By.CSS_SELECTOR, ".main-holder h1")


class ProductPageLocators:
    ICON_ADD_TO_FAVORITE = (By.CSS_SELECTOR, ".review-share .share mvid-icon[type='love']")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".tab-personal .number")
    FAVORITE_ICON_EMPTY = (By.CSS_SELECTOR, ".tab-personal .disabled")
    OPEN_FAV_PRODUCTS = (By.CSS_SELECTOR, ".tab-personal mvid-icon[type='love']")
    TITLE_SELECTED = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-title")
    NAME_PRODUCT_IN_FAV = (By.CSS_SELECTOR, ".wishlist-items-container .wishlist-item .wishlist-product-title a")
    COUNT_PRODUCTS_IN_FAV = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-quantity")
    DELETE_FROM_FAV_PRODUCT = (By.CSS_SELECTOR, ".wishlist-action-links .wishlist-delete-btn")
    TEXT_AFTER_DELETE = (By.CSS_SELECTOR, ".c-notifications .c-notifications__messages")
    CLOSE_AD = (By.CSS_SELECTOR, ".modal-layout__close")
