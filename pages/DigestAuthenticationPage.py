import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class DigestAuthenticationPage(BasePage):
    digestAuthenticationButton=(By.XPATH,'//*[@href="/digest_auth"]')
    succesContainer=(By.XPATH,'//*[@id="content"]/div/p')

    @keyword("Navigate Digest Authentication Page")
    def navigate_digest_authentication(self):
        self.click(self.digestAuthenticationButton)

    @keyword("Login Digest Authentication Page")
    def sendKeys_diget_authentication(self):
        authentication="https://admin:admin@the-internet.herokuapp.com/digest_auth"
        self.get_url(authentication)
        self.click(self.succesContainer)
        # burası sadece hoover,scroll,highlight,centercolour iceren bir utils ile
        # degistirilebilir
        # description_utils.py
        # element test eder
        # locatelistesi cikarir
        # korrdinatlarini verir
        # elementin tum ozelliklerini consola yazdırır
        # buton yada yazma kutusu uzerinde karasimsek efekti




def test_digest_authentication_tc01():
    driver_manager_page=DriverManagerPage()
    driver_manager_page.navigate_heroku_homePage()
    digest_authentication_page=DigestAuthenticationPage()
    digest_authentication_page.navigate_digest_authentication()
    digest_authentication_page.sendKeys_diget_authentication()


if __name__ == "__main__":
    test_digest_authentication_tc01()