import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time

from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage
from utils.description_utils import description_utils


class DynamicControlsPage(BasePage):
    dynamicControlsButton = (By.XPATH, '//*[@href="/dynamic_controls"]')
    checkbox = (By.XPATH, '//input[@type="checkbox"]')
    removeButton = (By.XPATH, '//button[.="Remove"]')
    message = (By.XPATH, '//button[@onclick="swapCheckbox()"]')
    addButton = (By.XPATH, '//button[@onclick="swapCheckbox()"]')
    itIsGoneMessage = (By.XPATH, '//*[@id="message"]')
    enabledButton=(By.XPATH,'//button[.="Enable"]')
    itIsEnabledMessage=(By.XPATH,'//*[@id="message"]')
    inputTextBox=(By.XPATH,'//input[@type="text"]')
    disableButton=(By.XPATH,'//button[.="Disable"]')
    itIsDisabledMessage=(By.XPATH,'//*[@id="message"]')

    @keyword("Navigate Dynamic Controls Page")
    def navigate_dynamic_controls(self):
        self.click(self.dynamicControlsButton)
    keyword("Click Checkbox")
    def click_checkbox(self):
        self.click(self.removeButton)

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.itIsGoneMessage))

        self.click(self.addButton)

        wait.until(EC.visibility_of_element_located(self.checkbox))

        self.click(self.checkbox)
        time.sleep(3)


    keyword("Enabled Button")
    def enabled_button(self):

        self.click(self.enabledButton)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.itIsEnabledMessage))

        self.write(self.inputTextBox,"test")
        self.click(self.disableButton)

        wait.until(EC.visibility_of_element_located(self.itIsDisabledMessage))

        self.click(self.enabledButton)






def test_dynamic_controls_test():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.click_checkbox()
    driver_manager.close_driver()

def test_dynamic_controls_test2():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.enabled_button()
    driver_manager.close_driver()

def test_mixed_checkbox_and_remove_argument():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_controls_page = DynamicControlsPage()
    dynamic_controls_page.navigate_dynamic_controls()
    dynamic_controls_page.click_checkbox()
    time.sleep(3)
    dynamic_controls_page.enabled_button()



if __name__ == "__main__":
    test_dynamic_controls_test()