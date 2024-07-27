import pytest

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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


@pytest.mark.route('resizable')
@pytest.mark.xfail('Dependency on screen resolution')
class TestResizablePage:
    def test_resizable_box(self, driver):
        resizable_page = ResizablePage(driver)
        default_size, min_size, max_size = resizable_page.change_size_resizable_box()
        # assert default_size == ('200px', '200px')
        # assert min_size == ('150px', '150px')
        # assert min_size == ('500px', '300px')
        print(default_size)
        print(min_size)
        print(max_size)

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver)
        min_size, max_size = resizable_page.change_size_resizable()
        # assert min_size == ('20px', '20px')
        # assert max_size == ('500px', '300px')
        print(min_size)
        print(max_size)




