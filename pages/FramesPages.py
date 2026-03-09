from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FramesPages(BasePage):
    frameTop=(By.XPATH, "//frame[@name='frame-top']")
    frameBottom=(By.XPATH, "//frame[@name='frame-bottom']")
    leftframetop=(By.XPATH, "//frame[@name='frame-left']")
    middleframetop=(By.XPATH, "//frame[@name='frame-middle']")
    rightframebottom=(By.XPATH, "//frame[@name='frame-right']")
    leftLetter=(By.XPATH, "//body[text()='LEFT']")
    middleLetter=(By.XPATH, "//div[@id='content' and text()='MIDDLE']")

    @keyword("Navigate to Frames Examples Pages")
    def navigate_to_frames_pages(self):
        self.click(self.framePagesLinkButton)


    @keyword("Navigate to Nested Frames Examples Pages")
    def navigate_to_nested_frames_pages(self):
       self.click(self.nestedFramesLinkButton)

    @keyword("Nested Frames Print Text")
    def nested_frames_print_text(self):
        self.click(self.leftFramesLinkButton)
        self.click(self.middleFrameLinkButton)
        self.click(self.rightFrameLinkButton)



def test_nested_frames_print_text():
    driver_manager_page = DriverManagerPage()
    frames_page=FramesPages()
    driver_manager_page.navigate_heroku_homePage()
    frames_page.navigate_to_nested_frames_pages()
    frames_page.nested_frames_print_text()
    driver_manager_page.close_driver()

if __name__ == "__main__":
    test_nested_frames_print_text()



