import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self, tab):
        tabs = {'tab_list': {
            'title': self.locators.TAB_LIST,
            'list': self.locators.TAB_LIST_ITEMS,
        },
            'tab_grid': {
                'title': self.locators.TAB_GRID,
                'list': self.locators.TAB_GRID_ITEMS
            }}
        self.element_is_visible(tabs[tab]['title']).click()
        order_before = self.get_sortable_items(tabs[tab]['list'])
        items_to_drag = random.sample(self.elements_are_visible(tabs[tab]['list']), k=2)
        item_what = items_to_drag[0]
        item_where = items_to_drag[1]
        self.drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(tabs[tab]['list'])
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def select_list_item(self, tab):
        tabs = {'tab_list': {
            'title': self.locators.TAB_LIST,
            'list': self.locators.LIST_ITEM,
            'active_list': self.locators.LIST_ITEM_ACTIVE,
        },
            'tab_grid': {
                'title': self.locators.TAB_GRID,
                'list': self.locators.GRID_ITEM,
                'active_list': self.locators.GRID_ITEM_ACTIVE,
            }}
        self.element_is_visible(tabs[tab]['title']).click()
        item_list = self.elements_are_visible(tabs[tab]['list'])

        for item in item_list:
            item.click()

        item_list_active = self.elements_are_visible(tabs[tab]['active_list'])

        return len(item_list), len(item_list_active)


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_pixels_from_width_height(self, size_value):
        width = size_value.split(';')[0].split(':')[1].replace(' ', '')
        height = size_value.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_min_max_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        default_size = self.get_pixels_from_width_height(self.get_min_max_size(self.locators.RESIZABLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -50, -50)
        min_size = self.get_pixels_from_width_height(self.get_min_max_size(self.locators.RESIZABLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_pixels_from_width_height(self.get_min_max_size(self.locators.RESIZABLE_BOX))
        return default_size, min_size, max_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), 100, 100)
        max_size = self.get_pixels_from_width_height(self.get_min_max_size(self.locators.RESIZABLE))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), -200, -200)
        min_size = self.get_pixels_from_width_height(self.get_min_max_size(self.locators.RESIZABLE))
        return min_size, max_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def simple_drag_and_drop(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_element = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_element = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        text_before_drop = drop_element.text
        self.drag_and_drop_to_element(drag_element, drop_element)
        return text_before_drop, drop_element.text

    def accept_drag_and_drop(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_element = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_element = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_element = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)

        self.drag_and_drop_to_element(not_acceptable_element, drop_element)
        drop_element_text_with_no_accept = drop_element.text

        self.drag_and_drop_to_element(acceptable_element, drop_element)
        drop_element_text_with_accept = drop_element.text
        return drop_element_text_with_no_accept, drop_element_text_with_accept

    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_element = self.element_is_visible(self.locators.DRAG_ME_PROPOGATION)

        not_greedy_inner_box = self.element_is_present(self.locators.NOT_GREEDY_INNER_BOX)
        self.drag_and_drop_to_element(drag_element, not_greedy_inner_box)
        text_not_greedy_outer_box = self.element_is_present(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text

        greedy_inner_box = self.element_is_present(self.locators.GREEDY_INNER_BOX)
        self.drag_and_drop_to_element(drag_element, greedy_inner_box)
        text_greedy_outer_box = self.element_is_present(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text

        return text_not_greedy_outer_box, text_not_greedy_inner_box, text_greedy_outer_box, text_greedy_inner_box

    def drop_with_revert_drop(self, drag_type):
        drops = {
            'will_revert': {
                'revert': self.locators.WILL_REVERT},
            'not_revert': {
                'revert': self.locators.NOT_REVERT}}

        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        revert = self.element_is_visible(drops[drag_type]['revert'])
        drop_here = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.drag_and_drop_to_element(revert, drop_here)

        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert