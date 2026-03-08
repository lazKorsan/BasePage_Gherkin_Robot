from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage

class ExitIntentPage(BasePage):
    exitIntentButton = (By.XPATH, '//*[@href="/exit_intent"]')
    flashMessages = (By.XPATH, '//*[@id="flash-messages"]')
    modalCloseButton=(By.XPATH,'//p[.="Close"]')

    @keyword("Navigate Exit Intent Page")
    def navigate_exit_intent_page(self):
        self.click(self.exitIntentButton)

    @keyword("Action Mouse Move To Out Of The Viewport")
    def action_mouse_move_to_out_of_the_viewport(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.TAG_NAME, "html")
        actions.move_to_element(element).move_by_offset(0, -int(element.size['height'] / 2) - 20).perform()

    @keyword("Wait For Flash Message To Appear")
    def wait_for_flash_message_to_appear(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.flashMessages))

    @keyword("Push Modal Close Button")
    def push_modal_close_button(self):
        self.click(self.modalCloseButton)




def test_exit_intent_page():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    exit_intent_page = ExitIntentPage()
    exit_intent_page.navigate_exit_intent_page()
    exit_intent_page.action_mouse_move_to_out_of_the_viewport()
    exit_intent_page.wait_for_flash_message_to_appear()
    exit_intent_page.push_modal_close_button()
    driver_manager.close_driver()