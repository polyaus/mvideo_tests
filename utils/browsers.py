from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def build_browser():
    prefs = {"profile.default_content_setting_values.notifications": 2}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--window-size=1320,1080')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
