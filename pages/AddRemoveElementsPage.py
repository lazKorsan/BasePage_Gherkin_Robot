


import sys
import os

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from selenium.webdriver.common.by import By
import time
from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class AddRemoveElementsPage(BasePage):
    addRemoveElementsButton = (By.XPATH, '//*[@href="/add_remove_elements/"]')
    addElementsButton =(By.XPATH, '//*[@onclick="addElement()"]')
    deleteButton =(By.XPATH, '//*[@onclick="deleteElement()"]')

    @keyword("Navigate Add Remove Elements Page")
    def navigate_addRemoveElements(self):
        self.click(self.addRemoveElementsButton)
        time.sleep(3)
    @keyword("Add Elements")
    def add_elements(self):
        self.click(self.addElementsButton)
        time.sleep(3)

    @keyword("Delete Elements")
    def delete_elements(self):
        self.click(self.deleteButton)
        time.sleep(3)


def test_US002_tc01():
    driver_manager_page = DriverManagerPage()
    addRemoveElementsPage = AddRemoveElementsPage()
    driver_manager_page.navigate_heroku_homePage()
    addRemoveElementsPage.navigate_addRemoveElements()
    addRemoveElementsPage.add_elements()
    addRemoveElementsPage.delete_elements()
    driver_manager_page.close_driver()




