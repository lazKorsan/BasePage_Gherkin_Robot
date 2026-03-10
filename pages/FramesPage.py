import sys
import os

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FramesPage(BasePage):
    framesPageButton = (By.XPATH, '//*[@id="content"]/ul/li[22]/a')
    nestedFramesButton = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')

    @keyword("Navigate to Nested Frame Page")
    def navigate_to_nested_frame_page(self):
        self.click(self.framesPageButton)
        self.click(self.nestedFramesButton)
    @keyword("Get Text from Nested Frame Left Frame")
    def get_text_left_frame(self):
        # Üst çerçeveye geçiş (frame-top)
        self.driver.switch_to.frame("frame-top")
        # Sol çerçeveye geçiş (frame-left)
        self.driver.switch_to.frame("frame-left")
        # LEFT metnini bul ve yazdır
        left_element = self.driver.find_element(By.XPATH, "//body")
        print("LEFT:", left_element.text)
        # Kapsayıcıdan çık
        self.driver.switch_to.parent_frame()
    @keyword("Get Text from Nested Frame Middle Frame")
    def get_text_middle_frame(self):
        # Orta çerçeveye geçiş (frame-middle)
        self.driver.switch_to.frame("frame-middle")
        # MIDDLE metnini bul ve yazdır
        middle_element = self.driver.find_element(By.XPATH, "//div[@id='content']")
        print("MIDDLE:", middle_element.text)
        # Kapsayıcıdan çık
        self.driver.switch_to.parent_frame()
    @keyword("Get Text from Nested Frame Right Frame")
    def get_text_right_frame(self):
        # Sağ çerçeveye geçiş (frame-right)
        self.driver.switch_to.frame("frame-right")
        # RIGHT metnini bul ve yazdır
        right_element = self.driver.find_element(By.XPATH, "//body")
        print("RIGHT:", right_element.text)
        # Asıl çerçeveye geri dön
        self.driver.switch_to.default_content()
    @keyword("Get Text from Nested Frame Bottom Frame")
    def get_text_bottom_frame(self):
        # Alt çerçeveye geçiş (frame-bottom)
        self.driver.switch_to.frame("frame-bottom")
        # BOTTOM metnini bul ve yazdır
        bottom_element = self.driver.find_element(By.XPATH, "//body")
        print("BOTTOM:", bottom_element.text)
        # Asıl çerçeveye geri dön
        self.driver.switch_to.default_content()


class TestFrames(object):
    def test_get_text_from_nested_frame(self):
        driver_manager_page = DriverManagerPage()
        driver_manager_page.navigate_heroku_homePage()
        page = FramesPage()
        page.navigate_to_nested_frame_page()

        page.get_text_left_frame()


def test_get_text_left():
    driver_manager_page = DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    page = FramesPage()
    page.navigate_to_nested_frame_page()
    page.get_text_left_frame()
    page.get_text_middle_frame()
    page.get_text_right_frame()
    page.get_text_bottom_frame()
    driver_manager_page.close_driver()