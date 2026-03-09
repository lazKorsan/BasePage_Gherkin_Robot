from pages.DriverManagerPage import DriverManagerPage
from pages.ForgotPasswordPage import ForgotPasswordPage


def test_forgot_password():
    email="lazKorsan@gmail.com"
    driver_manager_page= DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    page=ForgotPasswordPage()
    page.click_forgot_password_link_button()
    page.send_email(userMail=email)
    page.click_forgot_password()
    driver_manager_page.close_driver()