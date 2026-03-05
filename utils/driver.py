from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Driver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # Buradaki ayarlar driver'ın hayatta kalmasını sağlar
            service = Service(ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service)
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None