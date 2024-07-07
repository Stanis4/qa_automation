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
