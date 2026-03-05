from pages.DriverManagerPage import DriverManagerPage


def test_driverManagerPage_correction():
    driver_manager_page = DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    driver_manager_page.close_driver()