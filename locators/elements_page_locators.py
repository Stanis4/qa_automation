from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ITEM_TITLE = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    # add person info
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class='close']")

    # table data
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    PARENT_RAW = (".//ancestor::div[@class='rt-tr-group']")
    LAST_ROW = ("//div[@class='rt-tr-group'][string-length() > 8][last()]")  # last not empty row
    FILLED_ROW = ("//div[@class='rt-tr-group'][string-length() > 8]")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    ROWS_NUMBER = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "div[class=-previous]")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div[class=-next]")

    # update
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me'] ")

    # result messages
    DOUBLE_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    UNAUTHORISED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")


class UploadAndDownloadPageLocators:
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='uploadFile']")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")


