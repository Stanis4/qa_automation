from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutocompletePageLocators:
    MULTIPLE_NAMES_BUTTON = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_NAMES_VALUES = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTIPLE_NAMES_REMOVE_ITEM = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] '
                                                   'svg path')
    MULTIPLE_NAMES_REMOVE_ALL_ITEMS = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"] svg path')

    SINGLE_NAME_BUTTON = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_NAME_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class SliderPageLocators:
    SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_TEXT_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarPageLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")
    PROGRESS_BAR_COMPLETED = (By.CSS_SELECTOR, "div[class='progress-bar bg-success']")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[id='resetButton']")


class TabsPageLocators:
    TAB_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TAB_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TAB_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TAB_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TAB_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")


class TooltipsPageLocators:
    HOVER_BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    HOVER_BUTTON_TOOLTIP = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    TEXT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TEXT_FIELD_TOOLTIP = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_WORD = (By.XPATH, '//*[.="Contrary"]')
    CONTRARY_WORD_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    NUMBER_WORD = (By.XPATH, '//*[.="1.10.32"]')
    NUMBER_WORD_TOOLTIP = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOLTIPS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


class MenuSelectPageLocators:
    # Select value
    SELECT_VALUE_DROPDOWN = (By.CSS_SELECTOR, 'div[id="withOptGroup"]')
    SELECT_VALUE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-2-input"]')
    SELECT_DROPDOWN_VALUE = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')

    # Select one value
    SELECT_ONE_DROPDOWN = (By.CSS_SELECTOR, 'div[id="selectOne"]')
    OPTION_DR = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-0"]')
    OPTION_MR = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-1"]')
    OPTION_MRS = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-2"]')
    OPTION_MS = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-3"]')
    OPTION_PROF = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-4"]')
    OPTION_OTHER = (By.CSS_SELECTOR, 'div[id="react-select-3-option-0-5"]')

    # old style select
    OLD_STYLE_SELECT_MENU = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    # multi select drop down
    MULTISELECT_DROPDOWN = (By.XPATH, "(//div[@class=' css-yk16xz-control'])[3]")
    MULTISELECT_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    MULTISELECT_INPUT_LIST = (By.XPATH, "//div[@class=' css-11unzgr']/*")
    CLEAR_BUTTON = (By.CSS_SELECTOR, "svg[class='css-19bqh2r']")
    NO_OPTIONS = (By.CSS_SELECTOR, "div[class=' css-1gl4k7y']")
    LIST_OF_OPTIONS = (By.XPATH, "//div[@class=' css-11unzgr']/*")
    LIST_OF_ADDED_OPTIONS = (By.CSS_SELECTOR, "div[class ='css-1rhbuit-multiValue']")


    # standard select
    STANDARD_MULTISELECT = (By.CSS_SELECTOR, 'select[id="cars"]')


