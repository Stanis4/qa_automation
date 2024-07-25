import pytest

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@pytest.mark.route('browser-windows')
class TestBrowserWindows:

    def test_new_tab(self, driver):
        new_tab_page = BrowserWindowsPage(driver)
        result_text, current_url = new_tab_page.check_new_opened_tab()
        assert result_text[0] == "This is a sample page"
        assert current_url[1] == "https://demoqa.com/sample"


@pytest.mark.route('alerts')
class TestAlertsPage:

    def test_see_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alert_text = alerts_page.check_see_alert()
        assert alert_text == "You clicked a button"

    def test_see_alert_in_5_sec(self, driver):
        alerts_page = AlertsPage(driver)
        alert_text = alerts_page.check_see_alert_in_5_sec()
        assert alert_text == "This alert appeared after 5 seconds"

    def test_confirm_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alert_text, alert_result_text = alerts_page.check_confirm_alert()
        assert alert_text == "Do you confirm action?"
        assert alert_result_text == "You selected Ok"

    def test_prompt_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alert_text, alert_result_text = alerts_page.check_prompt_alert()
        assert alert_text == "Please enter your name"
        assert alert_result_text == "You entered test"


@pytest.mark.route('frames')
class TestFramesPage:

    def test_frames(self, driver):
        frames_page = FramesPage(driver)
        frame1 = frames_page.check_frame('frame1')
        frame2 = frames_page.check_frame('frame2')
        assert frame1 == ['This is a sample page', '500px', '350px'], 'Frame is not available'
        assert frame2 == ['This is a sample page', '100px', '100px'], 'Frame is not available'


@pytest.mark.route('nestedframes')
class TestNestedFramesPage:

    def test_nested_frames(self, driver):
        nested_frames_page = NestedFramesPage(driver)
        parent_text, child_text = nested_frames_page.check_nested_frame()
        assert parent_text == 'Parent frame', 'Parent frame is not found'
        assert child_text == 'Child Iframe', 'Child frame is not found'


@pytest.mark.route('modal-dialogs')
class TestModalDialogsPage:

    def test_modal_dialogs(self, driver):
        modal_dialogs_page = ModalDialogsPage(driver)
        small_modal, large_modal = modal_dialogs_page.check_modal_dialogs()
        assert small_modal[1] < large_modal[1]
        assert small_modal[0] == 'Small Modal', f'Header for small modal is wrong: {small_modal[0]}'
        assert large_modal[0] == 'Large Modal', f'Header for large modal is wrong: {large_modal[0]}'
