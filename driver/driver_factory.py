
from selenium import webdriver

import config


def driver_factory(browser_name: str):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        return webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        return getattr(webdriver, config.browser.capitalize())()
