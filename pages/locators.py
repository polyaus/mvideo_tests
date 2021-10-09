from selenium.webdriver.common.by import By


class BasePageLocators:
    BODY = (By.CSS_SELECTOR, "body")
    CLOSE_AD = (By.CSS_SELECTOR, ".modal-layout__close")


class MainPageLocators(BasePageLocators):
    LOCATION = (By.CSS_SELECTOR, ".location .location-text")
    # LOCATION_SELECTED = (By.CSS_SELECTOR, "#header-city-selection-link .header-top-line__link-text")
    INPUT_CITY = (By.CSS_SELECTOR, ".location-select__input-wrap input[placeholder=\"Ваш город\"]")
    LIST_CITIES = (By.CSS_SELECTOR, ".location-selection__container .location-select__location")
    FAVORITES_ICON = (By.CSS_SELECTOR, ".header-icon__icon .i-icon-fl-favorite")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".tab-personal .bubble")


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.CSS_SELECTOR, ".header-main .header-icon_default .i-icon-fl-profile")
    USER_CABINET = (By.CSS_SELECTOR, ".tab-profile .title")
    USERNAME = (By.CSS_SELECTOR, ".tooltip--visible .menu .tooltip__menu-link")
    LOGOUT = (By.CSS_SELECTOR, ".tooltipster-sidetip-profile .header-user__actions a[data-holder='#signout']")
    LOGIN_WITH_PASSWORD = (By.CSS_SELECTOR, ".o-login__login .c-link[data-holder=\"#useEmailToEnter\"]")
    TELEPHONE = (By.CSS_SELECTOR, "#login-original")
    PASSWORD = (By.CSS_SELECTOR, "#login_password")
    ENTER_BTN = (By.CSS_SELECTOR, "#submit-button")
    CABINET_HEAD = (By.CSS_SELECTOR, ".main-holder h1")
    USER_ENTER = (By.CSS_SELECTOR, ".header-icon .header-icon__text")
    FAVORITES_HEADER = (By.CSS_SELECTOR, ".header-main__icon_wish .wishlist-amount")
    FAVORITES_FOOTER = (By.CSS_SELECTOR, ".my-account-wishlist .label-amount")
    EMPTY_FAVORITES_HEADER = (By.CSS_SELECTOR, ".header-main__icon_wish.header-icon_disabled")


class ProductPageLocators(BasePageLocators):
    PRODUCT_ADD_TO_FAVORITES = (By.CSS_SELECTOR, ".review-share .share mvid-icon[type='love']")
    FAVORITES_ICON_TOP = (By.CSS_SELECTOR, ".tab-personal .bubble")
    FAVORITE_ICON_ANIMATED = (By.CSS_SELECTOR, ".tab-personal .bubble.animated")
    ACTIVE_BTN_ADD_TO_FAVORITES = (By.CSS_SELECTOR, ".review-share .mv-icon-button--active")
    EMPTY_FAVORITES = (By.CSS_SELECTOR, ".tab-personal .disabled")
    OPEN_FAV_PRODUCTS = (By.CSS_SELECTOR, ".tab-personal mvid-icon[type='love']")
    AMOUNT_FAVORITES = (By.CSS_SELECTOR, ".header-main__icon_wish .wishlist-amount")
    EMPTY_WISH_LIST = (By.CSS_SELECTOR, ".header-main__icon_wish.header-icon_disabled")
    PRODUCT_ADD_TO_FAVORITES_LOGGED_USER = (By.CSS_SELECTOR, ".c-pdp-add-wishlist .c-blinking-text__unchecked")


class FavoritePageLocators(BasePageLocators):
    EMPTY_FAVORITES = (By.CSS_SELECTOR, ".whishlist-empty .whishlist-empty__title")
    FAVORITES = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-title")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".wishlist-items-container .wishlist-item .wishlist-product-title a")
    COUNT_IN_FAVORITES = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-quantity")
    DELETE_FAVORITES_BTN = (By.CSS_SELECTOR, ".wishlist-action-links .wishlist-delete-btn .i-icon-fl-trash")
    EMPTY_FAVORITES_AFTER_DELETE = (By.CSS_SELECTOR, ".c-notifications .c-notifications__title")
