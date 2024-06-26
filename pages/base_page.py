from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_are_not_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until_not(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_offset, y_offset):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_offset, y_offset)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove()")
        self.driver.execute_script("document.getElementById('close-fixedban').remove()")

    def switch_to_alert(self, timeout=6, is_accepted=True, data=None):
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        try:
            if data:
                alert.send_keys(data)
            alert_text = alert.text
        finally:
            if is_accepted:
                alert.accept()
            else:
                alert.dismiss()
        return alert_text

    def switch_to_frame(self, frame_locator, timeout=5):
        wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
