from pages.DriverManagerPage import DriverManagerPage
from pages.DropdownPage import DropdownPage


def test_simple_dropdown():
    """Basit dropdown test"""
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dropdown_page = DropdownPage()

    dropdown_page.navigate_dropdown()

    # En profesyonel yöntemi kullan
    dropdown_page.select_by_value_with_select_class("1")

    # Alternatif olarak:
    # dropdown_page.select_by_visible_text("Option 2")

    driver_manager.driver.quit()