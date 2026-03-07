from pages.DriverManagerPage import DriverManagerPage
from pages.DynamicContentPage import DynamicContentPage


def test_dynamic_content_tc02():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_content_page = DynamicContentPage()
    dynamic_content_page.navigate_dynamic_content()
    assert dynamic_content_page.verify_dynamic_content_changed() == True
    driver_manager.close_driver()