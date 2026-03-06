# C:\Users\user\PycharmProjects\use_BasePage\pages\ChallengingDomPage.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from pages.DriverManagerPage import DriverManagerPage

from pages.BasePage import BasePage


class ChallengingDomPage(BasePage):
    challengingDomButton = (By.XPATH, '//*[@href="/challenging_dom"]')
    cyanButton=(By.XPATH,'//*[@class="button"]')
    redButton=(By.XPATH,'//*[@class="button alert"]')
    greenButton=(By.XPATH,'//*[@class="button success"]')


    @keyword("Navigate Challenging Dom Page")
    def navigate_challenging_dom(self):
        self.click(self.challengingDomButton)
        time.sleep(3)
    @keyword("Description Color Button")
    def description_coulor_button(self):
        self.click(self.cyanButton)
        time.sleep(3)
        self.click(self.redButton)
        time.sleep(3)
        self.click(self.greenButton)
        time.sleep(3)


def test_challenging_dom():

    driver_manager_page = DriverManagerPage()
    challenging_dom_page = ChallengingDomPage()
    driver_manager_page.navigate_heroku_homePage()
    challenging_dom_page.navigate_challenging_dom()
    challenging_dom_page.description_coulor_button()
    driver_manager_page.close_driver()

if __name__ == "__main__":
    test_challenging_dom()