from utils.driver import Driver
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        """
        locator: (By.XPATH, "xpath_adresi") şeklinde geliyor.
        Biz sadece 'xpath_adresi' kısmını (ikinci eleman) alıyoruz.
        """
        xpath_value = locator[1] # Tuple'ın 2. elemanını al: locator[1]
        click_utils(self.driver, xpath_value)

    def write(self, locator, text):
        """
        Aynı şekilde locator içindeki sadece string olan XPATH'i gönderiyoruz.
        """
        xpath_value = locator[1]
        sendKey_utils(self.driver, xpath_value, text)