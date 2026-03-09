from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FramesPages(BasePage):
    userNameBox = (By.XPATH, '//input[@id="username"]')
    framePagesLinkButton=(By.XPATH,'//*[@id="content"]/ul/li[22]/a')
    nestedFramesLinkButton=(By.XPATH,'//*[@href="/nested_frames"]')
    iFramesLinkButton=(By.XPATH,'//*[@href="/iframe"]')
    leftFramesLinkButton=(By.XPATH,'//frame[@src="/frame_left"]')
    middleFrameLinkButton=(By.XPATH,'//*[@src="/frame_middle"]')
    rightFrameLinkButton=(By.XPATH,'//*[@src="/frame_right"]')
    bottomFrameLinkButton=(By.XPATH,'//frame[@src="/frame_bottom"]')
    topFrameContainer=(By.XPATH,'//html/frameset/frame[1]')

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



