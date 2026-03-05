import sys
import os
import time

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage




from pages.DriverManagerPage import DriverManagerPage

class BasicAuthPage(BasePage):
    basicAuthButton = (By.XPATH, '//*[@href="/basic_auth"]')
    _basic_auth_url_path = "the-internet.herokuapp.com/basic_auth"

    @keyword("Navigate Basic Auth Page")
    def navigate_basic_auth_Page(self):
        self.click(self.basicAuthButton)

    @keyword("Kullanici popUp menusune gecerli bilgileri girer")
    def user_enters_valid_info_into_popUpMenu(self, userName, password):

        auth_url = f"https://{userName}:{password}@{self._basic_auth_url_path}"
        self.get_url(auth_url)
        time.sleep(3)



if __name__ == "__main__":
    driver_manager_page = DriverManagerPage()
    basicAuthPage = BasicAuthPage()
    driver_manager_page.navigate_heroku_homePage()
    basicAuthPage.navigate_basic_auth_Page()
    basicAuthPage.user_enters_valid_info_into_popUpMenu("admin", "admin")

    driver_manager_page.close_driver()