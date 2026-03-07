import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class DropdownPage(BasePage):
    dropDownButton = (By.XPATH, '//*[@href="/dropdown"]')
    selectOptions=(By.XPATH,'//div/div/div/select')
    option1=(By.XPATH,'//div/div/div/select/option[2]')

    def navigate_dropdown(self):
        self.click(self.dropDownButton)

    def selecet_option(self):
        self.click(self.selectOptions)
        time.sleep(2)

    def options1(self):
        self.click(self.option1)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys('\ue007').perform()



















def test_dropDownMenu():
    driver_manager=DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dropdown_page=DropdownPage()
    dropdown_page.navigate_dropdown()
    dropdown_page.selecet_option()
    dropdown_page.options1()