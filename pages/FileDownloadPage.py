import sys
import os

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FileDownloadPage(BasePage):
    fileDownLoadButton = (By.XPATH, '//*[@href="/download"]')
    randonDataButton=(By.XPATH,'//*[@href="download/random_data.txt"]')
    @keyword("Navigate File Download Page")
    def navigate_file_download_page(self):
        self.click(self.fileDownLoadButton)
    @keyword("Download File")
    def download_file(self):
        self.click(self.randonDataButton)
        time.sleep(5)



def test_download_file():
    driver_manager = DriverManagerPage()
    try:
        driver_manager.navigate_heroku_homePage()
        file_download_page = FileDownloadPage()
        file_download_page.navigate_file_download_page()
        file_download_page.download_file()
    finally:
        driver_manager.close_driver()