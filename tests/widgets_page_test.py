import time

import pytest

from pages.widgets_page import AccordianPage, AutocompletePage, SliderPage, ProgressBarPage, TabsPage, TooltipsPage


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


class TestSlider:

    def test_slider_controller(self, driver):
        slider_page = SliderPage(driver, "https://demoqa.com/slider")
        slider_page.open()
        value_before, value_after, text_value_before, text_value_after = slider_page.change_slider_value()
        assert value_before != value_after
        assert text_value_before != text_value_after


class TestProgressBar:

    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        value_before, value_after = progress_bar_page.change_progress_bar_value()
        assert value_before != value_after

    def test_completed_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        completed_progress_bar, reset_value = progress_bar_page.complete_progress_bar()
        assert completed_progress_bar == '100%'
        assert reset_value == '0%'


class TestTabs:
    @pytest.mark.parametrize('tab, expected_title', [('what', 'What'), ('origin', 'Origin'), ('use', 'Use'), ('more', 'More')])
    def test_tabs(self, driver, tab, expected_title):
        tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
        tabs_page.open()
        tab_title, content_length = tabs_page.check_tabs(tab)
        assert tab_title == expected_title
        assert content_length > 0


class TestTooltips:
    def test_tooltips(self, driver):
        tooltips_page = TooltipsPage(driver, "https://demoqa.com/tool-tips")
        tooltips_page.open()
        tooltip_text_button, tooltip_text_field, tooltip_text_contrary, tooltip_text_number = tooltips_page.check_tooltips()
        assert tooltip_text_button == "You hovered over the Button"
        assert tooltip_text_field == "You hovered over the text field"
        assert tooltip_text_contrary == "You hovered over the Contrary"
        assert tooltip_text_number == "You hovered over the 1.10.32"