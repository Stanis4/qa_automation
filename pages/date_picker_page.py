from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from locators.date_picker_page_locators import DatePickerPageLocators
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_day_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        self.set_day_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        self.set_day_item_from_list(self.locators.DATE_TIME_YEAR_LIST, '2020')
        self.set_day_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_day_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_after = input_date_after.get_attribute("value")
        return value_date_before, value_date_after

    def set_date_by_text(self, element, text):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(text)

    def set_day_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
