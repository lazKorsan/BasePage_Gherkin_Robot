"""
US001AB_TestingPreCondition.py
C:\Users\user\PycharmProjects\use_BasePage\inLineTest\US001AB_TestingPreCondition.py
C:\Users\user\PycharmProjects\use_BasePage\pages\BasePage.py
C:\Users\user\PycharmProjects\use_BasePage\pages\DriverManagerPage.py
"""



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from selenium.webdriver.common.by import By
import time
from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class US001AB_TestingPreCondition(BasePage):
    AB_Testing_Button = (By.XPATH, '//*[@href="/abtest"]')
    testInfoContainer =(By.XPATH, '//*[@id="content"]/div/h3')
    infoContainer =(By.XPATH, '//*[@id="content"]/div/p/text()')
    poweredByLetter=(By.XPATH, '//*[@id="page-footer"]/div/div/text()')

    def navigate_AB_Testing(self):
        self.click(self.AB_Testing_Button)
        time.sleep(3)

    def AB_Testing_Container_element_koordinates(self):
        self.click(self.testInfoContainer)
        element = self.driver.find_element(*self.testInfoContainer)
        x = element.location['x']
        y = element.location['y']
        print(f"Elementin koordinatları: x={x}, y={y}")
        time.sleep(2)


    def info_section_element_koordinates(self):
        self.click(self.infoContainer)
        element = self.driver.find_element(*self.infoContainer)
        x = element.location['x']
        y = element.location['y']
        print(f"Elementin koordinatları: x={x}, y={y}")
        time.sleep(2)

    def poweredBy_letter_coordinates(self):
        self.click(self.poweredByLetter)
        element = self.driver.find_element(*self.poweredByLetter)
        x = element.location['x']
        y = element.location['y']
        print(f"Elementin koordinatları: x={x}, y={y}")
        time.sleep(2)


def test_powered_by_coordinates():
    driver_manager_page = DriverManagerPage()
    preConditionPage = US001AB_TestingPreCondition()
    driver_manager_page.navigate_heroku_homePage()
    preConditionPage.navigate_AB_Testing()
    preConditionPage.poweredBy_letter_coordinates()



def test_find_coordinates_poweredBy():
    driver_manager_page = DriverManagerPage()
    preConditionPage = US001AB_TestingPreCondition()
    driver_manager_page.navigate_heroku_homePage()
    preConditionPage.navigate_AB_Testing()
    preConditionPage.poweredBy_letter_coordinates()
    driver_manager_page.close_driver()


def test_find_coordinates_tc02():
    driver_manager_page = DriverManagerPage()
    preConditionPage = US001AB_TestingPreCondition()
    driver_manager_page.navigate_heroku_homePage()
    preConditionPage.navigate_AB_Testing()
    preConditionPage.info_section_element_koordinates()
    driver_manager_page.close_driver()




























