from pages.DriverManagerPage import DriverManagerPage
from pages.FileDownloadPage import FileDownloadPage


def test_download_file():
    driver_manager = DriverManagerPage()
    try:
        driver_manager.navigate_heroku_homePage()
        file_download_page = FileDownloadPage()
        file_download_page.navigate_file_download_page()
        file_download_page.download_file()
    finally:
        driver_manager.close_driver()