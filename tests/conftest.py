from datetime import datetime

import allure
import pytest
import config
from driver.driver_factory import driver_factory
from helpers import shared_driver


@pytest.fixture(scope='function')
def driver(request):
    url = config.browser.base_url
    if request.node.get_closest_marker('route'):
        url += request.node.get_closest_marker('route').args[0]
    driver = driver_factory(config.browser.type)
    shared_driver.driver = driver
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


# @pytest.fixture(scope='session', autouse=True)
# def os_properties():
#     allure_os_properties()


def pytest_exception_interact(node, call, report):
    try:
        attach = shared_driver.driver.get_screenshot_as_png()
        allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(e)
