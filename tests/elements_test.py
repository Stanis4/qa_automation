import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'full name not match'
            assert email == output_email, 'email not match'
            assert current_address == output_cur_addr, 'current address not match'
            assert permanent_address == output_perm_addr, 'permanent address not match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes are not selected'


class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "'Yes' was not selected"
        assert output_impressive == 'Impressive', "'Impressive' was not selected"
        assert output_no == 'No', "'No' was not selected"

    # check that 'No' radiobutton is disabled
    def test_no_button_is_disabled(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        no_button_clickable = radio_button_page.radio_button_no_status()
        assert no_button_clickable == 'No'


class TestWebTable:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person(count=7)
        result_table = web_table_page.check_new_added_person()
        for raw in new_person:
            assert raw in result_table, "entered record has not been added to the table"

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        keyword = web_table_page.add_new_person(count=1)[0][random.randint(0, 5)]
        result_table = web_table_page.check_new_added_person()
        for raw in result_table:
            assert raw in result_table, "entered record has not been added to the table"
        web_table_page.search_person(keyword=keyword)
        table_result = web_table_page.check_search_person()
        print(keyword)
        print(table_result)
        assert keyword in table_result, "person was not found in the table"


