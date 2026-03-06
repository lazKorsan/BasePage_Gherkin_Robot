from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--remote-allow-origins=*")
            
            # Selenium 4.6 ve sonrasi, driver'i otomatik olarak yonetir.
            # webdriver-manager'a ihtiyac kalmadi.
            cls._driver = webdriver.Chrome(options=chrome_options)
            
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
