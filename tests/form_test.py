import pytest

from pages.form_page import FormPage


@pytest.mark.route('automation-practice-form')
class TestFormPage:
    def test_form(self, driver):
        form_page = FormPage(driver)
        person_info = form_page.fill_form_fields()
        result = form_page.form_result()
        assert [person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]], \
            "Result form does not include expected values"
