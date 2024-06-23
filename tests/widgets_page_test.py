import time

import pytest

from pages.widgets_page import AccordianPage, AutocompletePage


class TestAccordianPage:

    @pytest.mark.parametrize('accordian_num, expected_title',
                             [('first', 'What is Lorem Ipsum?'),
                              ('second', 'Where does it come from?'),
                              ('third', 'Why do we use it?')])
    def test_accordian(self, driver, accordian_num, expected_title):
        accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
        accordian_page.open()
        actual_title, actual_content_len = accordian_page.check_accordian(accordian_num)
        assert actual_title == expected_title
        assert actual_content_len > 0


class TestAutocompletePage:

    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        add_colors = autocomplete_page.fill_multi_colors()
        add_colors_result = autocomplete_page.check_colors_in_multi()
        assert add_colors == add_colors_result

    def test_remove_item_from_multi(self, driver):
        autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        autocomplete_page.fill_multi_colors()
        count_values_before, count_values_after = autocomplete_page.remove_value_from_multi()
        assert count_values_before > count_values_after

    def test_remove_all_items_from_multi(self, driver):
        autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        autocomplete_page.fill_multi_colors()
        list_before, list_after = autocomplete_page.remove_all_from_multi()
        assert list_before > list_after
        assert list_after == 0

    def test_single_color_input(self, driver):
        autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
        autocomplete_page.open()
        color = autocomplete_page.fill_single_input()
        color_result = autocomplete_page.check_single_color()
        assert color == color_result
