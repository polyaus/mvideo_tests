from selenium import webdriver


def build_browser():
    prefs = {"profile.default_content_setting_values.notifications": 2}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--window-size=1320,1080')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(chrome_options=chrome_options)
