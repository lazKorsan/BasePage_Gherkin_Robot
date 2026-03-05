# FormAuthenticationPage.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\FormAuthenticationPage.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\BasePage.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\click_utils.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\driver.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\sendkey_utils.py
#
#

import sys
import os

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from pages.DriverManagerPage import DriverManagerPage
from pages.BasePage import BasePage


class FormAuthenticationPage(BasePage):
    formAuthenticationButton = (By.XPATH, '//*[@href="/login"]')
    userName = "user"
    password = "pass!"
    userNameBox = (By.XPATH, '//input[@id="username"]')
    passwordBox = (By.XPATH, '//*[@id="password"]')
    submitButton = (By.XPATH, '//*[@class="fa fa-2x fa-sign-in"]')

    @keyword("Navigate Form Authentication Page")
    def navigate_formAuthentication_Page(self):
        self.click(self.formAuthenticationButton)

    @keyword("User logs in with valid credentials")
    def user_logs_in_with_valid_credentials(self, userName, password):
        self.write(self.userNameBox, self.userName)
        self.write(self.passwordBox, self.password)
        self.click(self.submitButton)


if __name__ == "__main__":
    driver_manager_page = DriverManagerPage()
    formAuthenticationPage = FormAuthenticationPage()
    driver_manager_page.navigate_heroku_homePage()
    formAuthenticationPage.navigate_formAuthentication_Page()
    formAuthenticationPage.user_logs_in_with_valid_credentials( "user", "pass!")
    driver_manager_page.close_driver()





























































