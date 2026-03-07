from pages.Drag_and_DropPage import Drag_and_DropPage
from pages.DriverManagerPage import DriverManagerPage


def test_drag_and_drop_tc03():
    driver_manager_page = DriverManagerPage()
    drag_and_drop_page = Drag_and_DropPage()
    driver_manager_page.navigate_heroku_homePage()
    drag_and_drop_page.drag_and_drop_easy_way()
    driver_manager_page.close_driver()