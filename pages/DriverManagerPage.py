
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword
from pages.BasePage import BasePage

class DriverManagerPage(BasePage):  # Düzeltildi
    heroku_URL = "https://the-internet.herokuapp.com/"

    @keyword("Navigate Heroku Home Page")
    def navigate_heroku_homePage(self):
        self.get_url(self.heroku_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)



    @keyword("Close Driver")
    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    driver_manager_page = DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    driver_manager_page.close_driver()
