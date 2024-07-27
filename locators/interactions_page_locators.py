from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    TAB_LIST_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    TAB_GRID_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle '
                                      'react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span[class='react-resizable-handle "
                                         "react-resizable-handle-se']")

