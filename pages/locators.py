from selenium.webdriver.common.by import By


class BasePageLocators:
    BODY = (By.CSS_SELECTOR, "body")


class MainPageLocators(BasePageLocators):
    LOCATION = (By.CSS_SELECTOR, "#header-city-selection-link .header-top-line__link-text")
    CITY_INPUT = (By.CSS_SELECTOR, "#region-selection-form-city-input")
    GIVEN_CITY = (By.CSS_SELECTOR, ".city-selection-popup-results a")
    FAVORITE_ICON_BUTTON = (By.CSS_SELECTOR, ".header-icon__icon .i-icon-fl-favorite")
    TEXT_EMPTY_FAV_LIST = (By.CSS_SELECTOR, ".whishlist-empty .whishlist-empty__title")
    AMOUNT_WISHLIST = (By.CSS_SELECTOR, ".header-main__icon_wish .wishlist-amount")
    CLOSE_AD = (By.CSS_SELECTOR, ".c-popup.c-popup_facelift")


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.CSS_SELECTOR, ".header-main .header-icon_default .i-icon-fl-profile")
    USER = (By.CSS_SELECTOR, ".tab-profile .title")
    USERNAME = (By.CSS_SELECTOR, ".tooltip--visible .menu .tooltip__menu-link")
    LOGOUT = (By.CSS_SELECTOR, ".tooltipster-sidetip-profile .header-user__actions a[data-holder='#signout']")
    ENTER_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".o-login__login .c-link")
    TELEPHONE = (By.CSS_SELECTOR, "#login-original")
    PASSWORD = (By.CSS_SELECTOR, "#login_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit-button")
    CABINET_HEAD = (By.CSS_SELECTOR, ".main-holder h1")
    TEXT_ON_BUTTON_ENTER = (By.CSS_SELECTOR, ".header-icon .header-icon__text")
    COUNT_PROD_IN_FAV_FROM_LP_UP = (By.CSS_SELECTOR, ".header-main__icon_wish .wishlist-amount")
    COUNT_PROD_IN_FAV_FROM_LP_DOWN = (By.CSS_SELECTOR, ".my-account-wishlist .label-amount")
    EMPTY_WISH_LIST = (By.CSS_SELECTOR, ".header-main__icon_wish.header-icon_disabled")


class ProductPageLocators(BasePageLocators):
    ICON_ADD_TO_FAVORITE = (By.CSS_SELECTOR, ".review-share .share mvid-icon[type='love']")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".tab-personal .bubble")
    FAVORITE_ICON_ANIMATED = (By.CSS_SELECTOR, ".tab-personal .bubble.animated")
    ACTIVE_FAVORITE_ICON = (By.CSS_SELECTOR, ".review-share .mv-icon-button--active")
    FAVORITE_ICON_EMPTY = (By.CSS_SELECTOR, ".tab-personal .disabled")
    OPEN_FAV_PRODUCTS = (By.CSS_SELECTOR, ".tab-personal mvid-icon[type='love']")
    CLOSE_AD = (By.CSS_SELECTOR, ".modal-layout__close")
    AMOUNT_WISHLIST = MainPageLocators.AMOUNT_WISHLIST
    EMPTY_WISH_LIST = (By.CSS_SELECTOR, ".header-main__icon_wish.header-icon_disabled")
    ICON_ADD_TO_FAVORITE_AUTH_USER = (By.CSS_SELECTOR, ".c-pdp-add-wishlist .c-blinking-text__unchecked")


class FavoritePageLocators(BasePageLocators):
    TEXT_EMPTY_FAVORITE_LIST = (By.CSS_SELECTOR, ".whishlist-empty .whishlist-empty__title")
    TITLE_SELECTED = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-title")
    NAME_PRODUCT_IN_FAV = (By.CSS_SELECTOR, ".wishlist-items-container .wishlist-item .wishlist-product-title a")
    COUNT_PRODUCTS_IN_FAV = (By.CSS_SELECTOR, ".wishlist-topline .wishlist-quantity")
    DELETE_FROM_FAV_PRODUCT = (By.CSS_SELECTOR, ".wishlist-action-links .wishlist-delete-btn .i-icon-fl-trash")
    TEXT_AFTER_DELETE = (By.CSS_SELECTOR, ".c-notifications .c-notifications__title")
