import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, SliderPageLocators, \
    ProgressBarPageLocators, TabsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutocompletePage(BasePage):
    locators = AutocompletePageLocators()

    def fill_multi_colors(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 11))
        for color in colors:
            multi_input = self.element_is_clickable(self.locators.MULTIPLE_NAMES_BUTTON)
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_values_before = len(self.elements_are_present(self.locators.MULTIPLE_NAMES_VALUES))
        remove_button_list = self.elements_are_present(self.locators.MULTIPLE_NAMES_REMOVE_ITEM)
        for value in remove_button_list:
            value.click()
            break
        count_values_after = len(self.elements_are_present(self.locators.MULTIPLE_NAMES_VALUES))
        return count_values_before, count_values_after

    # remove colors altogether with the x button
    def remove_all_from_multi(self):
        count_values_before = len(self.elements_are_present(self.locators.MULTIPLE_NAMES_VALUES))
        self.element_is_visible(self.locators.MULTIPLE_NAMES_REMOVE_ALL_ITEMS).click()
        count_values_after = len(self.elements_are_not_present(self.locators.MULTIPLE_NAMES_VALUES))
        return count_values_before, count_values_after

    def check_colors_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTIPLE_NAMES_VALUES)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_NAME_BUTTON)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_single_color(self):
        color = self.element_is_visible(self.locators.SINGLE_NAME_VALUE).text
        return color


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER).get_attribute('value')
        text_value_before = self.element_is_visible(self.locators.SLIDER_TEXT_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER)
        random_value = random.randint(-255, 256)
        if value_before == random_value:
            random_value += 1
        self.action_drag_and_drop_by_offset(slider_input, random_value, 0)
        value_after = self.element_is_visible(self.locators.SLIDER).get_attribute('value')
        text_value_after = self.element_is_visible(self.locators.SLIDER_TEXT_VALUE).get_attribute('value')
        return value_before, value_after, text_value_before, text_value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('style')
        start_stop_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        start_stop_button.click()
        time.sleep(random.randint(1, 7))
        start_stop_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('style')
        return value_before, value_after

    def complete_progress_bar(self):
        start_stop_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        start_stop_button.click()
        completed_progress_bar = self.element_is_present(self.locators.PROGRESS_BAR_COMPLETED, timeout=15).text
        reset_button = self.element_is_visible(self.locators.RESET_BUTTON)
        reset_button.click()
        reset_value = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return completed_progress_bar, reset_value


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name):
        tabs = {
            'what': {
                'title': self.locators.TAB_WHAT,
                'content': self.locators.TAB_WHAT_CONTENT},
            'origin': {
                'title': self.locators.TAB_ORIGIN,
                'content': self.locators.TAB_ORIGIN_CONTENT},
            'use': {
                'title': self.locators.TAB_USE,
                'content': self.locators.TAB_USE_CONTENT},
            'more': {
                'title': self.locators.TAB_MORE,
                'content': None}}

        button = self.element_is_visible(tabs[tab_name]['title'])
        button.click()
        content = self.element_is_visible(tabs[tab_name]['content']).text
        return button.text, len(content)
