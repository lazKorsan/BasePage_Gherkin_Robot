from pages.CheckboxesPage import CheckboxesPage
from pages.DriverManagerPage import DriverManagerPage


def test_checboxes_press_in_order_test():
    driver_manager_page = DriverManagerPage()
    checkboxes=CheckboxesPage()
    driver_manager_page.navigate_heroku_homePage()
    checkboxes.navigate_checkboxes()
    checkboxes.press_in_order_checkboxes()
    driver_manager_page.close_driver()