from pages.DriverManagerPage import DriverManagerPage
from pages.FormAuthenticationPage import FormAuthenticationPage


def test_fill_form_authentication():
    driver_manager_page = DriverManagerPage()
    formAuthenticationPage = FormAuthenticationPage()
    driver_manager_page.navigate_heroku_homePage()
    formAuthenticationPage.navigate_formAuthentication_Page()
    formAuthenticationPage.user_logs_in_with_valid_credentials("user", "pass!")
    driver_manager_page.close_driver()