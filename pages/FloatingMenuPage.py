import time

from robot.api.deco import keyword
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FloatingMenuPage(BasePage):
    floatingMenuButton = (By.XPATH, '//*[@href="/floating_menu"]')
    objectText10=(By.XPATH,'//*[@id="content"]/div/div[2]/div/p[10]')
    homeButton=(By.XPATH,'//*[@id="menu"]/ul/li[1]/a')

    @keyword("Navigate Folating Menu Page")
    def navigate_floating_menu_page(self):
        self.click(self.floatingMenuButton)

    @keyword("Scroll to Given Numbers of Object Text")
    def scroll_to_object_text_nd(self):
        self.click(self.objectText10)
        time.sleep(3)


    @keyword("Definition one Of Menu Button spacially Home Buttonare ")
    def home_button_description_and_click(self):
        self.click(self.homeButton)

















def test_floating_menu():
    driver_manager = DriverManagerPage()
    try:
        driver_manager.navigate_heroku_homePage()
        floating_menu_page = FloatingMenuPage()
        floating_menu_page.navigate_floating_menu_page()
        floating_menu_page.scroll_to_object_text_nd()
        floating_menu_page.home_button_description_and_click()
    finally:
        driver_manager.close_driver()





































