import pytest

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragablePage


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


@pytest.mark.route('droppable')
class TestDroppablePage:
    def test_simple_drop(self, driver):
        droppable_page = DroppablePage(driver)
        text_before_drop, text_after_drop = droppable_page.simple_drag_and_drop()
        assert text_before_drop == "Drop here"
        assert text_after_drop == "Dropped!"

    def test_accept_drop(self, driver):
        droppable_page = DroppablePage(driver)
        drop_element_text_with_no_accept, drop_element_text_with_accept = droppable_page.simple_drag_and_drop()
        assert drop_element_text_with_no_accept == "Drop here"
        assert drop_element_text_with_accept == "Dropped!"

    def test_prevent_drop(self, driver):
        droppable_page = DroppablePage(driver)
        not_greedy_outer, not_greedy_inner, greedy_outer, greedy_inner = droppable_page.drop_prevent_propogation()
        assert not_greedy_outer == "Dropped!"
        assert not_greedy_inner == "Dropped!"
        assert greedy_outer == "Outer droppable"
        assert greedy_inner == "Dropped!"

    @pytest.mark.parametrize('drag_type', [('will_revert'), ('not_revert')])
    def test_revert_drop(self, driver, drag_type):
        droppable_page = DroppablePage(driver)
        position_after_move, position_after_revert = droppable_page.drop_with_revert_drop(drag_type)
        if drag_type == 'will_revert':
            assert position_after_move != position_after_revert
        elif drag_type == 'not_revert':
            assert position_after_move == position_after_revert


@pytest.mark.route('dragabble')
class TestDragablePage:
    def test_simple_drag(self, driver):
        dragable_page = DragablePage(driver)
        before_position, after_position = dragable_page.simple_drag()
        assert before_position != after_position

    @pytest.mark.parametrize('drag_item', [('x'),('y')])
    def test_axis_restriction_drop(self, driver, drag_item):
        dragable_page = DragablePage(driver)
        top_item, left_item = dragable_page.axis_restricted(drag_item)
        if drag_item == 'x':
            assert top_item[0] == top_item[1]
            assert left_item[0] != left_item[1]
        elif drag_item == 'y':
            assert top_item[0] != top_item[1]
            assert left_item[0] == left_item[1]
