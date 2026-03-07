from pages.DriverManagerPage import DriverManagerPage
from pages.DynamicControlsPage import DynamicControlsPage


def test_mixed_checkbox_and_remove_argument():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.click_checkbox()
    dynamic_controls_page.enabled_button()
    driver_manager.close_driver()

def test_dynamic_controls_test2():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.enabled_button()
    driver_manager.close_driver()

def test_dynamic_controls_test():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.click_checkbox()
    driver_manager.close_driver()