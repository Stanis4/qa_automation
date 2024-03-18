import random

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


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
        new_person = web_table_page.add_new_person(count=5)
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
        assert keyword in table_result, "person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        person = web_table_page.add_new_person()
        last_name = person[0][1]
        web_table_page.search_person(last_name)
        edit_random_value = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert edit_random_value in row, f"value '{edit_random_value}' was not changed"

    def test_web_table_delete_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        person = web_table_page.add_new_person()
        email = person[0][3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found", "Record was not deleted"

    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        number_of_rows = web_table_page.select_number_of_rows()
        assert number_of_rows == [5, 10, 20, 25, 50, 100], "The number of rows was not changed"

    def test_web_table_switch_tables(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
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


class TestButtons:
    def test_button_click(self, driver):
        buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        buttons_page.open()
        double_click = buttons_page.double_click()
        right_click = buttons_page.right_click()
        click = buttons_page.click()
        assert double_click == "You have done a double click", "Double click action failed"
        assert right_click == "You have done a right click", "Right click action failed"
        assert click == "You have done a dynamic click", "Dynamic click action failed"


class TestLinksPage:
    def test_valid_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken"

    def test_status_codes(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
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


class TestUploadAndDownload:

    def test_upload_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download_page.open()
        file_name, result = upload_download_page.upload_file()
        assert file_name == result, "file was not uploaded"

    def test_download_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download_page.open()
        check = upload_download_page.download_file()
        assert check is True, "file was not downloaded"


class TestDynamicProperties:

    def test_dynamic_properties(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_color()
        assert color_before != color_after, "Button color was not changed"

    def test_button_enable_disable(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()
        disabled = dynamic_properties_page.check_button_is_disabled()
        enabled = dynamic_properties_page.check_button_is_enabled()
        assert disabled is True, "Disabled button is clickable"
        assert enabled is True, "Button was not enabled"
