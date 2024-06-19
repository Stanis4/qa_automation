import time

import pytest

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_opened_tab(self):
        buttons = [self.locators.NEW_TAB_BUTTON, self.locators.NEW_WINDOW_BUTTON]
        for button in buttons:
            self.element_is_visible(button).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_page_url = self.driver.current_url
            text_title = self.element_is_present(self.locators.NEW_PAGE_TEXT).text
            yield text_title, str(new_page_url)
            self.driver.switch_to.window(self.driver.window_handles[0])


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_in_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        return alert_window

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        text_result = self.element_is_present(self.locators.CONFIRM_TEXT_RESULT).text
        return alert_window, text_result

    def check_prompt_alert(self):
        text = 'test'
        self.element_is_visible(self.locators.PROMT_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert(data=text)
        text_result = self.element_is_present(self.locators.PROMT_TEXT_RESULT).text
        return alert_window, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num: str = None):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
        elif frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.switch_to_frame(frame)
        text = self.element_is_present(self.locators.FRAME_TEXT).text
        self.driver.switch_to.default_content()
        return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        title_small = self.element_is_visible(self.locators.SMALL_TITLE_MODAL).text
        body_small = self.element_is_visible(self.locators.SMALL_BODY_MODAL).text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()

        self.element_is_visible(self.locators.LARGE_MODAL).click()
        title_large = self.element_is_visible(self.locators.LARGE_TITLE_MODAL).text
        body_large = self.element_is_visible(self.locators.LARGE_BODY_MODAL).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()

        return [title_small, len(body_small)], [title_large, len(body_large)]


