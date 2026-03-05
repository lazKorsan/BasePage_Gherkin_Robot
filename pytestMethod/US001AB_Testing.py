from pages.AB_TestingPage import AB_TestingPage
from pages.DriverManagerPage import DriverManagerPage


def test_US001_TC01():
    driver_manager_page = DriverManagerPage()
    AB_testin_page = AB_TestingPage()
    driver_manager_page.navigate_heroku_homePage()
    AB_testin_page.navigate_AB_Testing()
    AB_testin_page.highlight_and_type_alphabet()
    driver_manager_page.close_driver()

def test_US001_TCO2():
    driver_manager_page = DriverManagerPage()
    AB_testin_page = AB_TestingPage()
    driver_manager_page.navigate_heroku_homePage()
    AB_testin_page.navigate_AB_Testing()
    AB_testin_page.highlight_and_type_with_delay("Merhaba Dunya", 150)
    driver_manager_page.close_driver()























