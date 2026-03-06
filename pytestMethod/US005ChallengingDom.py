from pages.ChallengingDomPage import ChallengingDomPage
from pages.DriverManagerPage import DriverManagerPage


def test_challenging_dom():

    driver_manager_page = DriverManagerPage()
    challenging_dom_page = ChallengingDomPage()
    driver_manager_page.navigate_heroku_homePage()
    challenging_dom_page.navigate_challenging_dom()
    challenging_dom_page.description_coulor_button()
    driver_manager_page.close_driver()