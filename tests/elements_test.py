import random

import pytest
import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.feature('Text Box')
@pytest.mark.route('text-box')
class TestTextBox:
    @allure.title('Test text box')
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver)
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
        assert full_name == output_name, 'full name not match'
        assert email == output_email, 'email not match'
        assert current_address == output_cur_addr, 'current address not match'
        assert permanent_address == output_perm_addr, 'permanent address not match'


@allure.feature('Check Box')
@pytest.mark.route('checkbox')
class TestCheckBox:
    @allure.title('Test check box')
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver)
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, 'checkboxes are not selected'


@allure.feature('Radio Button')
@pytest.mark.route('radio-button')
class TestRadioButton:
    @allure.title('Test Radio Button')
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver)
        radio_button_page.click_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "'Yes' was not selected"
        assert output_impressive == 'Impressive', "'Impressive' was not selected"
        assert output_no == 'No', "'No' was not selected"

    @allure.title('Test that no Radio Button is disabled')
    # check that 'No' radiobutton is disabled
    def test_no_button_is_disabled(self, driver):
        radio_button_page = RadioButtonPage(driver)
        no_button_clickable = radio_button_page.radio_button_no_status()
        assert no_button_clickable == 'No'


@allure.feature('Web Table')
@pytest.mark.route('webtables')
class TestWebTable:
    @allure.title('Test add person to web table')
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver)
        new_person = web_table_page.add_new_person(count=5)
        result_table = web_table_page.check_new_added_person()
        for raw in new_person:
            assert raw in result_table, "entered record has not been added to the table"

    @allure.title('Test search person in web table')
    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver)
        keyword = web_table_page.add_new_person(count=1)[0][random.randint(0, 5)]
        result_table = web_table_page.check_new_added_person()
        for raw in result_table:
            assert raw in result_table, "entered record has not been added to the table"
        web_table_page.search_person(keyword=keyword)
        table_result = web_table_page.check_search_person()
        assert keyword in table_result, "person was not found in the table"

    @allure.title('Test update person in web table')
    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver)
        person = web_table_page.add_new_person()
        last_name = person[0][1]
        web_table_page.search_person(last_name)
        edit_random_value = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert edit_random_value in row, f"value '{edit_random_value}' was not changed"

    @allure.title('Test delete person from web table')
    def test_web_table_delete_person_info(self, driver):
        web_table_page = WebTablePage(driver)
        person = web_table_page.add_new_person()
        email = person[0][3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found", "Record was not deleted"

    @allure.title('Test change count row in web table')
    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver)
        number_of_rows = web_table_page.select_number_of_rows()
        assert number_of_rows == [5, 10, 20, 25, 50, 100], "The number of rows was not changed"

    @allure.title('Test switch tables in web table')
    def test_web_table_switch_tables(self, driver):
        web_table_page = WebTablePage(driver)
        number_of_rows = web_table_page.change_number_of_rows(number=5)
        assert number_of_rows == 5

        web_table_page.add_new_person(count=5)
        number_of_all_rows = web_table_page.check_rows_number()
        number_of_filled_rows = web_table_page.check_filled_rows_number()
        assert number_of_all_rows == number_of_filled_rows

        web_table_page.go_to_next_table()
        number_of_all_rows = web_table_page.check_rows_number()
        number_of_filled_rows = web_table_page.check_filled_rows_number()
        assert number_of_all_rows == 5
        assert number_of_all_rows > number_of_filled_rows

        web_table_page.go_to_previous_table()
        assert number_of_all_rows == 5
        assert number_of_all_rows > number_of_filled_rows


@allure.feature('Buttons')
@pytest.mark.route('buttons')
class TestButtons:
    @allure.title('Test button click')
    def test_button_click(self, driver):
        buttons_page = ButtonsPage(driver)
        double_click = buttons_page.double_click()
        right_click = buttons_page.right_click()
        click = buttons_page.click()
        assert double_click == "You have done a double click", "Double click action failed"
        assert right_click == "You have done a right click", "Right click action failed"
        assert click == "You have done a dynamic click", "Dynamic click action failed"


@allure.feature('Links Page')
@pytest.mark.route('links')
class TestLinksPage:
    @allure.title('Test valid link')
    def test_valid_link(self, driver):
        links_page = LinksPage(driver)
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken"

    @allure.title('Test status codes')
    def test_status_codes(self, driver):
        links_page = LinksPage(driver)
        bad_link = links_page.check_link("https://demoqa.com/bad-request")
        created_link = links_page.check_link("https://demoqa.com/created")
        no_content_link = links_page.check_link("https://demoqa.com/no-content")
        moved_link = links_page.check_link("https://demoqa.com/moved")
        unauthorized_link = links_page.check_link("https://demoqa.com/unauthorized")
        forbidden_link = links_page.check_link("https://demoqa.com/forbidden")
        not_found_link = links_page.check_link("https://demoqa.com/invalid-url")
        assert bad_link == 400
        assert created_link == 201
        assert no_content_link == 204
        assert moved_link == 301
        assert unauthorized_link == 401
        assert forbidden_link == 403
        assert not_found_link == 404


@allure.feature('Upload - Download')
@pytest.mark.route('upload-download')
class TestUploadAndDownload:
    @allure.title('Test upload file')
    def test_upload_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver)
        file_name, result = upload_download_page.upload_file()
        assert file_name == result, "file was not uploaded"

    @allure.title('Test download file')
    def test_download_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver)
        check = upload_download_page.download_file()
        assert check is True, "file was not downloaded"


@allure.feature('Dynamic Properties')
@pytest.mark.route('dynamic-properties')
class TestDynamicProperties:

    @allure.title('Test dynamic properties')
    def test_dynamic_properties(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        color_before, color_after = dynamic_properties_page.check_changed_color()
        assert color_before != color_after, "Button color was not changed"

    @allure.title('Test disabling and enabling of button')
    def test_button_enable_disable(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        disabled = dynamic_properties_page.check_button_is_disabled()
        enabled = dynamic_properties_page.check_button_is_enabled()
        assert disabled is True, "Disabled button is clickable"
        assert enabled is True, "Button was not enabled"
