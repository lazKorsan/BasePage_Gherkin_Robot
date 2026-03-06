from pages.DigestAuthenticationPage import DigestAuthenticationPage
from pages.DriverManagerPage import DriverManagerPage


def test_digest_authentication_tc01():
    driver_manager_page=DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    digest_authentication_page=DigestAuthenticationPage()
    digest_authentication_page.navigate_digest_authentication()
    digest_authentication_page.sendKeys_diget_authentication()