import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class DynamicLoadingPage(BasePage):
    dynamicLoadingButton = (By.XPATH, '//*[@href="/dynamic_loading"]')
    example1Button = (By.XPATH, '//*[@href="/dynamic_loading/1"]')
    example2Button = (By.XPATH, '//*[@href="/dynamic_loading/2"]')
    startButton = (By.XPATH, '//*[@id="start"]/button')
    helloWorldMessage = (By.XPATH, '//h4[normalize-space()="Hello World!"]')

    @keyword("Navigate Dynamic Loading Page")
    def navigate_dynamic_loading(self):
        self.click(self.dynamicLoadingButton)
    keyword("Click Example1")
    def click_example1(self):
        self.click(self.example1Button)
    keyword("Click Start for Example1")
    def click_start_for_example1(self):
        self.click(self.startButton)

        wait = WebDriverWait(self.driver, 10)
        # Wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located(self.helloWorldMessage))
        print(element.text)
    keyword("Click Example2")
    def click_example2(self):
        self.click(self.example2Button)

    keyword("Click Start for Example2")
    def click_start_for_example2(self):
        self.click(self.startButton)

        wait = WebDriverWait(self.driver, 10)
        # Wait for the element to be visible
        element = wait.until(EC.visibility_of_element_located(self.helloWorldMessage))
        print(element.text)







def test_dynamic_loading():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_loading_page = DynamicLoadingPage()
    dynamic_loading_page.navigate_dynamic_loading()
    dynamic_loading_page.click_example1()
    dynamic_loading_page.click_start_for_example1()
    driver_manager.close_driver()


if __name__ == "__main__":
    test_dynamic_loading()



def test_dynamic_loading2():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_loading_page = DynamicLoadingPage()
    dynamic_loading_page.navigate_dynamic_loading()
    dynamic_loading_page.click_example2()
    dynamic_loading_page.click_start_for_example2()
    driver_manager.close_driver()

if __name__ == "__main__":
    test_dynamic_loading2()

