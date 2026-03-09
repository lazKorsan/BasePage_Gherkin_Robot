import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time


from robot.api.deco import keyword
from selenium.webdriver.common.by import By


from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class FileUploadPage(BasePage):
    fileUploadButton = (By.XPATH, '//*[@href="/upload"]')
    upLoadFilePath="C:\\Users\\user\\PycharmProjects\\use_BasePage\\3d_difdenk.png"
    chooseFileButton=(By.XPATH,'//input[@id="file-upload"]')
    upLoadButton=(By.XPATH,'//input[@id="file-submit"]')
    upLoadFilesName="3d_difdenk.png"
    upLoadedFilesContainer=(By.XPATH,'//*[@id="uploaded-files"]')
    upLoadFilesNameContainer=(By.XPATH,'//*[@id="uploaded-files"]')


    @keyword("Navigate File Upload Page")
    def navigate_file_upload_page(self):
        self.click(self.fileUploadButton)

    @keyword("File Upload Process")
    def file_upload_process(self):
        self.write(self.chooseFileButton,self.upLoadFilePath)
        self.click(self.upLoadButton)
        time.sleep(1)
    @keyword("Assert Up Load File Name")
    def assert_up_load_file_name(self):
        expected_file_name="3d_difdenk.png"
        uploaded_files_element = self.driver.find_element(*self.upLoadedFilesContainer)
        uploaded_files_text = uploaded_files_element.text
        print(uploaded_files_text)
        assert expected_file_name in uploaded_files_text, f"Expected file '{expected_file_name}' not found in uploaded files. Found: {uploaded_files_text}"









def test_file_upload():
    driver_manager = DriverManagerPage()
    try:
        driver_manager.navigate_heroku_homePage()
        file_upload_page = FileUploadPage()
        file_upload_page.navigate_file_upload_page()
        file_upload_page.file_upload_process()
        file_upload_page.assert_up_load_file_name()
    finally:
        driver_manager.close_driver()

if __name__ == "__main__":
    test_file_upload()