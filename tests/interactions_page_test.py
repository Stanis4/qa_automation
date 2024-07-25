import pytest

from pages.interactions_page import SortablePage, SelectablePage


@pytest.mark.route('sortable')
@pytest.mark.parametrize('tab', [('tab_list'), ('tab_grid')])
class TestSortablePage:
    def test_sortable(self, driver, tab):
        sortable_page = SortablePage(driver)
        order_before, order_after = sortable_page.change_list_order(tab)
        assert order_before != order_after


@pytest.mark.route('selectable')
@pytest.mark.parametrize('tab', [('tab_list'), ('tab_grid')])
class TestSelectablePage:
    def test_selectable(self, driver, tab):
        selectable_page = SelectablePage(driver)
        default_list_len, active_list_len = selectable_page.select_list_item(tab)
        assert default_list_len == active_list_len



