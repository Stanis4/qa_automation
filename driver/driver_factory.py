
from selenium import webdriver

import config


def driver_factory(browser_name: str):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        return getattr(webdriver, config.browser.capitalize())()
