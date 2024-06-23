import random

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators
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

