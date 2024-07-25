import random
import time

import pytest

from pages.widgets_page import AccordianPage, AutocompletePage, SliderPage, ProgressBarPage, TabsPage, TooltipsPage, \
    MenuPage, MenuSelectPage


@pytest.mark.route('accordian')
class TestAccordianPage:

    @pytest.mark.parametrize('accordian_num, expected_title',
                             [('first', 'What is Lorem Ipsum?'),
                              ('second', 'Where does it come from?'),
                              ('third', 'Why do we use it?')])
    def test_accordian(self, driver, accordian_num, expected_title):
        accordian_page = AccordianPage(driver)
        actual_title, actual_content_len = accordian_page.check_accordian(accordian_num)
        assert actual_title == expected_title
        assert actual_content_len > 0


@pytest.mark.route('auto-complete')
class TestAutocompletePage:

    def test_fill_multi_autocomplete(self, driver):
        autocomplete_page = AutocompletePage(driver)
        add_colors = autocomplete_page.fill_multi_colors()
        add_colors_result = autocomplete_page.check_colors_in_multi()
        assert add_colors == add_colors_result

    def test_remove_item_from_multi(self, driver):
        autocomplete_page = AutocompletePage(driver)
        autocomplete_page.fill_multi_colors()
        count_values_before, count_values_after = autocomplete_page.remove_value_from_multi()
        assert count_values_before > count_values_after

    def test_remove_all_items_from_multi(self, driver):
        autocomplete_page = AutocompletePage(driver)
        autocomplete_page.fill_multi_colors()
        list_before, list_after = autocomplete_page.remove_all_from_multi()
        assert list_before > list_after
        assert list_after == 0

    def test_single_color_input(self, driver):
        autocomplete_page = AutocompletePage(driver)
        color = autocomplete_page.fill_single_input()
        color_result = autocomplete_page.check_single_color()
        assert color == color_result


@pytest.mark.route('slider')
class TestSlider:

    def test_slider_controller(self, driver):
        slider_page = SliderPage(driver)
        value_before, value_after, text_value_before, text_value_after = slider_page.change_slider_value()
        assert value_before != value_after
        assert text_value_before != text_value_after


@pytest.mark.route('progress-bar')
class TestProgressBar:

    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver)
        value_before, value_after = progress_bar_page.change_progress_bar_value()
        assert value_before != value_after

    def test_completed_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver)
        completed_progress_bar, reset_value = progress_bar_page.complete_progress_bar()
        assert completed_progress_bar == '100%'
        assert reset_value == '0%'


@pytest.mark.route('tabs')
class TestTabs:
    @pytest.mark.parametrize('tab, expected_title',
                             [('what', 'What'), ('origin', 'Origin'), ('use', 'Use'), ('more', 'More')])
    def test_tabs(self, driver, tab, expected_title):
        tabs_page = TabsPage(driver)
        tab_title, content_length = tabs_page.check_tabs(tab)
        assert tab_title == expected_title
        assert content_length > 0


@pytest.mark.route('tool-tips')
class TestTooltips:
    def test_tooltips(self, driver):
        tooltips_page = TooltipsPage(driver)
        tooltip_text_button, tooltip_text_field, tooltip_text_contrary, tooltip_text_number = tooltips_page.check_tooltips()
        assert tooltip_text_button == "You hovered over the Button"
        assert tooltip_text_field == "You hovered over the text field"
        assert tooltip_text_contrary == "You hovered over the Contrary"
        assert tooltip_text_number == "You hovered over the 1.10.32"


@pytest.mark.route('menu')
class TestMenu:
    def test_menu(self, driver):
        menu_page = MenuPage(driver)
        expected_data = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                         'Sub Sub Item 2', 'Main Item 3']
        actual_data = menu_page.check_menu()
        assert expected_data == actual_data


@pytest.mark.route('select-menu')
class TestSelectMenu:
    input_values = [
        ("Group 1, option 1"),
        ("Group 1, option 2"),
        ("Group 2, option 1"),
        ("Group 2, option 2"),
        ("A root option"),
        ("Another root option")]

    @pytest.mark.parametrize('expected_value', input_values)
    def test_select_value(self, driver, expected_value):
        select_menu_page = MenuSelectPage(driver)
        actual_value = select_menu_page.check_select_value(expected_value)
        assert expected_value == actual_value

    input_values = [("Dr."), ("Mr."), ("Mrs."), ("Ms."), ("Prof."), ("Other")]

    @pytest.mark.parametrize('expected_value', input_values)
    def test_select_one_value(self, driver, expected_value):
        select_menu_page = MenuSelectPage(driver)
        inserted_value = select_menu_page.check_select_one_value(expected_value)
        assert expected_value == inserted_value

    color = random.choice(["Blue", "Green", "Yellow", "White", "Indigo", "Magenta", "Aqua", "Red"])

    @pytest.mark.parametrize('expected_value', [color])
    def test_old_style_select(self, driver, expected_value):
        select_menu_page = MenuSelectPage(driver)
        value_before, value_after = select_menu_page.check_old_style_select(expected_value)
        assert value_before != value_after

    def test_multiselect(self, driver):
        select_menu_page = MenuSelectPage(driver)
        options_len, num_of_added_options = select_menu_page.insert_multiselect_values()
        assert options_len != 0
        assert num_of_added_options != 0
        assert options_len == num_of_added_options

    def test_standard_multiselect_with_one_select(self, driver):
        select_menu_page = MenuSelectPage(driver)
        background_color_before, background_color_after = select_menu_page.select_one_value_in_standard_multiselect()
        assert background_color_before != background_color_after

    def test_standard_multiselect_with_multiple_select(self, driver):
        select_menu_page = MenuSelectPage(driver)
        list_of_rgba = select_menu_page.select_multiple_values_in_standard_multiselect()
        assert 'rgba(0, 0, 0, 0)' not in list_of_rgba

