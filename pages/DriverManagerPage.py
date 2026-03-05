from robot.api.deco import keyword

from pages.BasePage import BasePage


class DriverMangerPage(BasePage):
    heroku_URL="https://the-internet.herokuapp.com/"

    @keyword("Navigate Heroku Home Page")
    def navigate_heroku_homePage(self):
        self.get_url(self.heroku_URL)
    @keyword("Close Driver")
    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    driver_manager_page = DriverMangerPage()
    driver_manager_page.navigate_heroku_homePage()
    driver_manager_page.close_driver()