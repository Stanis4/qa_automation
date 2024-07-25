import pytest
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from driver.driver_factory import driver_factory


@pytest.fixture(scope='function')
def driver(request):
    url = config.browser.base_url
    if request.node.get_closest_marker('route'):
        url += request.node.get_closest_marker('route').args[0]
    driver = driver_factory(config.browser.type)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
