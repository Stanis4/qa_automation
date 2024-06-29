from pages.date_picker_page import DatePickerPage


class TestTextBox:
    def test_select_date(self, driver):
        date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        old_date, new_date = date_picker_page.select_date()
        assert old_date != new_date

    def test_select_date_and_time(self, driver):
        date_time_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
        date_time_picker_page.open()
        old_date, new_date = date_time_picker_page.select_date_and_time()
        assert old_date != new_date
