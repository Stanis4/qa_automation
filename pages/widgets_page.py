import random
import time
from selenium.webdriver.support.select import Select

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, SliderPageLocators, \
    ProgressBarPageLocators, TabsPageLocators, TooltipsPageLocators, MenuPageLocators, MenuSelectPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


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
        completed_progress_bar = self.element_is_present(self.locators.PROGRESS_BAR_COMPLETED).text
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


class TooltipsPage(BasePage):
    locators = TooltipsPageLocators()

    def get_text_from_tooltips(self, hover_element, wait_element):
        element = self.element_is_visible(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        time.sleep(0.3)
        tooltip_text = self.element_is_visible(self.locators.TOOLTIPS)
        return tooltip_text.text

    def check_tooltips(self):
        tooltip_text_button = self.get_text_from_tooltips(self.locators.HOVER_BUTTON,
                                                          self.locators.HOVER_BUTTON_TOOLTIP)
        tooltip_text_field = self.get_text_from_tooltips(self.locators.TEXT_FIELD, self.locators.TEXT_FIELD_TOOLTIP)
        tooltip_text_contrary = self.get_text_from_tooltips(self.locators.CONTRARY_WORD,
                                                            self.locators.CONTRARY_WORD_TOOLTIP)
        tooltip_text_number = self.get_text_from_tooltips(self.locators.NUMBER_WORD, self.locators.NUMBER_WORD_TOOLTIP)
        return tooltip_text_button, tooltip_text_field, tooltip_text_contrary, tooltip_text_number


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class MenuSelectPage(BasePage):
    locators = MenuSelectPageLocators()

    def check_select_value(self, key):
        input_field = self.element_is_visible(self.locators.SELECT_VALUE_INPUT)
        input_field.send_keys(key)
        input_field.send_keys(Keys.ENTER)
        text_value = self.element_is_visible(self.locators.SELECT_DROPDOWN_VALUE)
        return text_value.text

    def check_select_one_value(self, option):
        options = {
            'Dr.': {
                'title': self.locators.OPTION_DR},
            'Mr.': {
                'title': self.locators.OPTION_MR},
            'Mrs.': {
                'title': self.locators.OPTION_MRS},
            'Ms.': {
                'title': self.locators.OPTION_MS},
            'Prof.': {
                'title': self.locators.OPTION_PROF},
            'Other': {
                'title': self.locators.OPTION_OTHER}}

        input_field = self.element_is_visible(self.locators.SELECT_ONE_DROPDOWN)
        input_field.click()
        select_one_dropdown = self.element_is_visible(options[option]['title'])
        select_one_dropdown.click()
        selected_value = self.element_is_visible(self.locators.SELECT_DROPDOWN_VALUE)
        return selected_value.text

    def check_old_style_select(self, text):
        option_field = self.element_is_visible(self.locators.OLD_STYLE_SELECT_MENU)
        value_before = option_field.get_attribute('value')
        option_field.click()
        self._select_option_by_text(option_field, text)
        value_after = option_field.get_attribute('value')
        return value_before, value_after

    def _select_option_by_text(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    def insert_multiselect_values(self):
        input_dropdown = self.element_is_visible(self.locators.MULTISELECT_DROPDOWN)
        input_dropdown.click()
        input_field = self.element_is_visible(self.locators.MULTISELECT_INPUT)
        options = options_len = len(self.elements_are_present(self.locators.LIST_OF_OPTIONS))
        while options_len >= 1:
            input_field.send_keys(Keys.ENTER)
            options_len -= 1
        assert self.element_is_visible(self.locators.NO_OPTIONS)
        num_of_added_options = len(self.elements_are_visible(self.locators.LIST_OF_ADDED_OPTIONS))
        return options, num_of_added_options

    def select_one_value_in_standard_multiselect(self):
        random_car = random.choice(['volvo', 'saab', 'opel', 'audi'])
        random_car_locator = (By.CSS_SELECTOR, f"select[id='cars'] option[value='{random_car}']")
        select_box = self.element_is_visible(self.locators.STANDARD_MULTISELECT)
        random_car_object = self.element_is_visible(random_car_locator)

        background_color_before = random_car_object.value_of_css_property('background-color')
        select_item = Select(select_box)
        select_item.select_by_value(random_car)
        background_color_after = random_car_object.value_of_css_property('background-color')
        return background_color_before, background_color_after

    def select_multiple_values_in_standard_multiselect(self):
        car_list = ['volvo', 'saab', 'opel', 'audi']
        select_box = self.element_is_visible(self.locators.STANDARD_MULTISELECT)
        list_of_rgba = []
        for car in car_list:
            locator = (By.CSS_SELECTOR, f"select[id='cars'] option[value='{car}']")
            car_object = self.element_is_visible(locator)
            select_item = Select(select_box)
            select_item.select_by_value(car)
            background_color_of_item = car_object.value_of_css_property('background-color')
            list_of_rgba.append(background_color_of_item)
        return list_of_rgba
