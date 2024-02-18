import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablePageLocators, ButtonsPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        SUBMIT_BTN = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(SUBMIT_BTN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_visible(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            item_title = box.find_element('xpath', self.locators.ITEM_TITLE)
            data.append(item_title.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_radio_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON,
                   }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

    def radio_button_no_status(self):
        return self.element_is_clickable(self.locators.NO_BUTTON).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        persons = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            persons.append([firstname, lastname, str(age), email, str(salary), department])
        print(persons)
        return persons

    def check_new_added_person(self):
        people_list = self.elements_are_visible(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keyword):
        search_box = self.element_is_visible(self.locators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        self.go_to_element(delete_button)
        row = delete_button.find_element("xpath", self.locators.LAST_ROW)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        parameters = {person_info.first_name: self.locators.FIRSTNAME_INPUT,
                      person_info.email: self.locators.EMAIL_INPUT,
                      str(person_info.age): self.locators.AGE_INPUT,
                      str(person_info.salary): self.locators.SALARY_INPUT,
                      person_info.department: self.locators.DEPARTMENT_INPUT}

        random_parameter = random.choice(list(parameters.keys()))
        edit_button = self.element_is_visible(self.locators.EDIT_BUTTON)
        self.go_to_element(edit_button)
        edit_button.click()
        self.element_is_visible(parameters[random_parameter]).clear()
        self.element_is_visible(parameters[random_parameter]).send_keys(str(random_parameter))
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(random_parameter)

    def delete_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        self.go_to_element(delete_button)
        delete_button.click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_number_of_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            row_number_button = self.element_is_visible(self.locators.ROWS_NUMBER)
            self.go_to_element(row_number_button)
            row_number_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_rows_number())
        return data

    def check_rows_number(self):
        number_of_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(number_of_rows)

    def check_filled_rows_number(self):
        number_of_filled_rows = self.elements_are_present((By.XPATH, self.locators.FILLED_ROW))
        return len(number_of_filled_rows)

    def change_number_of_rows(self, number):
        row_number_button = self.element_is_visible(self.locators.ROWS_NUMBER)
        self.go_to_element(row_number_button)
        row_number_button.click()
        self.element_is_visible((By.CSS_SELECTOR, f"option[value='{number}']")).click()
        return self.check_rows_number()

    def go_to_next_table(self):
        self.element_is_clickable(self.locators.NEXT_BUTTON).click()

    def go_to_previous_table(self):
        self.element_is_clickable(self.locators.PREVIOUS_BUTTON).click()


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click(self):
        click_button = self.element_is_visible(self.locators.CLICK_BUTTON)
        click_button.click()
        return self.check_click_result(self.locators.CLICK_BUTTON_MESSAGE)

    def double_click(self):
        double_click_button = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.go_to_element(double_click_button)
        self.action_double_click(double_click_button)
        return self.check_click_result(self.locators.DOUBLE_CLICK_BUTTON_MESSAGE)

    def right_click(self):
        right_click_button = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        self.go_to_element(right_click_button)
        self.action_right_click(right_click_button)
        return self.check_click_result(self.locators.RIGHT_CLICK_BUTTON_MESSAGE)

    def check_click_result(self, element):
        return self.element_is_present(element).text

