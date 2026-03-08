from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage

class StorageExitİntentPage(BasePage):
    exitIntentButton = (By.XPATH, '//*[@href="/exit_intent"]')
    flashMessages = (By.XPATH, '//*[@id="flash-messages"]')

    @keyword("Navigate Exit Intent Page")
    def navigate_exit_intent_page(self):
        self.click(self.exitIntentButton)

    @keyword("Action Mouse Move To Out Of The Viewport")
    def action_mouse_move_to_out_of_the_viewport(self):
        actions = ActionChains(self.driver)
        # Move the mouse to coordinates outside of the viewport
        actions.move_by_offset(650, -10).perform()

    @keyword("Wait For Flash Message To Appear")
    def wait_for_flash_message(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.flashMessages))


def test_exit_intent_page():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    exit_intent_page = StorageExitİntentPage()
    exit_intent_page.navigate_exit_intent_page()
    exit_intent_page.action_mouse_move_to_out_of_the_viewport()
    exit_intent_page.wait_for_flash_message()  # Wait for the flash message
