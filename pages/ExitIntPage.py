import time

import pyautogui
from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage

class ExitIntentPage(BasePage):
    exitIntentButton = (By.XPATH, '//*[@href="/exit_intent"]')
    flashMessages = (By.XPATH, '//*[@id="flash-messages"]')
    modalCloseButton=(By.XPATH,'//p[.="Close"]')

    @keyword("Navigate Exit Intent Page")
    def navigate_exit_intent_page(self):
        self.click(self.exitIntentButton)

    @keyword("Action Mouse Move To Out Of The Viewport")
    def action_mouse_move_to_out_of_the_viewport(self):
        print("3 saniye içinde fareyi hareket ettireceğim...")
        print("Fareyi hareket ettirmek istemiyorsan şimdi Ctrl+C yap")
        time.sleep(3)

        # Ekran çözünürlüğünü al
        screen_width, screen_height = pyautogui.size()

        # Sayfanın tam ortası
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Fareyi önce ekranın ortasına götür (kontrol amaçlı)
        pyautogui.moveTo(center_x, center_y, duration=0.6)
        time.sleep(0.5)

        # Çoğu tarayıcıda adres çubuğuna yaklaşık konumlar (1920×1080 için)
        # Bu değerler ekran çözünürlüğüne ve tarayıcıya göre değişir!

        # Firefox / Chrome / Edge için yaklaşık adres çubuğu konumu
        url_bar_x = screen_width // 2  # genellikle yatayda ortada
        url_bar_y = int(screen_height * 0.04)  # ekranın üstünden %4 aşağıda

        # Daha güvenli bir yöntem: üstten sabit piksel aşağı inmek
        # url_bar_y = 60   # 40-80 arası çoğu tarayıcıda çalışır

        print(f"Fareyi şu konuma taşıyorum: ({url_bar_x}, {url_bar_y})")

        # Fareyi adres çubuğuna taşı
        pyautogui.moveTo(url_bar_x, url_bar_y, duration=0.8)

        # İstersen tıklamasını da sağlayabilirsin:
        time.sleep(0.3)
        # pyautogui.click()          # sol tıklama
        # pyautogui.doubleClick()    # çift tıklama (adres çubuğunu seçer)

        print("Fare adres çubuğuna getirildi.")

    @keyword("Wait For Flash Message To Appear")
    def wait_for_flash_message_to_appear(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.flashMessages))

    @keyword("Push Modal Close Button")
    def push_modal_close_button(self):
        self.click(self.modalCloseButton)


def test_mouse_move():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    exit_intent_page = ExitIntentPage()
    exit_intent_page.navigate_exit_intent_page()
    exit_intent_page.action_mouse_move_to_out_of_the_viewport()
    exit_intent_page.wait_for_flash_message_to_appear()
    exit_intent_page.push_modal_close_button()
    driver_manager.close_driver()

if __name__ == "__main__":
    test_mouse_move()