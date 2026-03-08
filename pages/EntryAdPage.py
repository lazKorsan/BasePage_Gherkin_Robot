from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class EntryAdPage(BasePage):
    entryAdButton = (By.XPATH, '//*[@href="/entry_ad"]')
    clickHereButton=(By.XPATH,'//a[.="Click here"]')
    entryAdCloseButton=(By.XPATH,'//p[.="Close"]')

    @keyword("Navigate Entry Ad Page")
    def navigate_entry_ad_page(self):
        self.click(self.entryAdButton)
    @keyword("Push Modal Close Button")
    def  push_modal_close_button(self):
        self.click(self.entryAdCloseButton)



def test_modal_test():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    entry_ad_page = EntryAdPage()
    entry_ad_page.navigate_entry_ad_page()
    entry_ad_page.push_modal_close_button()
    driver_manager.close_driver()