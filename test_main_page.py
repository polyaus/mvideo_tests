from conftest import MAIN_PAGE_URL
from pages.mainpage import MainPage


def test_change_location_on_main_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    # main_page.close_ad_1()
    main_page.click_body()
    main_page.change_location_to_kaliningrad()
    main_page.check_location_is_kaliningrad()


def test_favorite_list_is_empty(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    # main_page.close_ad_1()
    main_page.open_favorite_list_from_main_page()
    main_page.favorite_list_is_empty()
