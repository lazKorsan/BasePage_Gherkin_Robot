from pages.AddRemoveElementsPage import AddRemoveElementsPage
from pages.DriverManagerPage import DriverManagerPage


def test_US002_tc01():
    driver_manager_page = DriverManagerPage()
    addRemoveElementsPage = AddRemoveElementsPage()
    driver_manager_page.navigate_heroku_homePage()
    addRemoveElementsPage.navigate_addRemoveElements()
    addRemoveElementsPage.add_elements()
    addRemoveElementsPage.delete_elements()
    driver_manager_page.close_driver()