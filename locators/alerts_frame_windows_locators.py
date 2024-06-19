from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_PAGE_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    #result text
    CONFIRM_TEXT_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMT_TEXT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    CLOSE_SMALL_MODAL = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    SMALL_TITLE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    SMALL_BODY_MODAL = (By.CSS_SELECTOR, "div[class='modal-body']")

    LARGE_MODAL = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    CLOSE_LARGE_MODAL = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    LARGE_TITLE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    LARGE_BODY_MODAL = (By.CSS_SELECTOR, "div[class='modal-body'] p")