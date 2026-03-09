import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class ForgotPasswordPage(BasePage):
    forgotPasswordLinkButton=(By.XPATH,'//*[@href="/forgot_password"]')
    emailBox=(By.XPATH,'//input[@id="email"]')
    retrievePasswordButton=(By.XPATH,'//button[@id="form_submit"]')
    email="lazKorsan@gmail.com"
    messageBox=(By.XPATH,'//html/body/h1')
    @keyword("Navigate Password Page")
    def click_forgot_password_link_button(self):
        self.click(self.forgotPasswordLinkButton)

    @keyword("Forgot Password Send Mail")
    def send_email(self,userMail):
        self.write(self.emailBox, self.email)
    @keyword("Click Forgot Password Button")
    def click_forgot_password(self):
        self.click(self.retrievePasswordButton)
        time.sleep(3)
        message = self.driver.find_element(*self.messageBox).text
        print(message)



def test_forgot_password():
    email="lazKorsan@gmail.com"
    driver_manager_page= DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    page=ForgotPasswordPage()
    page.click_forgot_password_link_button()
    page.send_email(userMail=email)
    page.click_forgot_password()
    driver_manager_page.close_driver()

