# US001AB_Testing.py
# C:\Users\user\PycharmProjects\use_BasePage\inLineTest\US001AB_Testing.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\BasePage.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\DriverManagerPage.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\click_utils.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\sendkey_utils.py
# C:\Users\user\PycharmProjects\use_BasePage\utils\driver.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\DriverManagerPage.py
# send basePage, driverManagerPage,
"""
sayfanın bosluk kısmına highlight edip harf yazdırmak istiyorum
fakat beceremedim.
test planım
sayfada bosluk kısma harf gondermek
bunun için ihtiyacım olan
sayfanın solt üst kösesine yakın
yatay  40 pixel
dikey 12 pixel lik bil alanı highlight edip
içine harf gondermek istiyorum.
şöyle bir şey olursa aslında çok iyi olur
highlight yapılan alana a yazar enter basar 150 milisaniye bekler
b yazar 150 mili saniye bekler
c .... z

"""

# US001AB_Testing.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class US001AB_Testing(BasePage):
    AB_Testing_Button = (By.XPATH, '//*[@href="/abtest"]')

    def navigate_AB_Testing(self):
        self.click(self.AB_Testing_Button)
        time.sleep(3)

    def highlight_and_type_alphabet(self):
        """
        Sayfanın sol üst köşesine yakın bir noktaya tıklar ve
        alfabeyi yazdırır (a'dan z'ye)
        """
        # Sol üst köşeye yakın koordinatlar (40px yatay, 12px dikey)
        x = 40
        y = 12

        try:
            # Koordinatlardaki elementi bul
            element = self.driver.execute_script("return document.elementFromPoint(arguments[0], arguments[1]);", x, y)

            if element:
                # Elementi highlight et (kırmızı çerçeve)
                self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
                self.driver.execute_script("arguments[0].style.transition='border 0.5s'", element)

                # Elemente tıkla
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()

                # Alfabeyi yazdır
                for harf in 'abcdefghijklmnopqrstuvwxyz':
                    actions = ActionChains(self.driver)
                    actions.send_keys(harf)
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    time.sleep(0.15)  # 150 milisaniye bekle

                    print(f"Yazıldı: {harf}")

                print("Alfabe başarıyla yazdırıldı!")
            else:
                print(f"Koordinatlarda element bulunamadı: ({x}, {y})")

        except Exception as e:
            print(f"Hata oluştu: {str(e)}")

    def highlight_and_type_with_delay(self, text, delay_ms=150):
        """
        Belirtilen metni karakter karakter yazar

        Args:
            text (str): Yazılacak metin
            delay_ms (int): Karakterler arası bekleme süresi (milisaniye)
        """
        x = 40
        y = 12

        try:
            element = self.driver.execute_script("return document.elementFromPoint(arguments[0], arguments[1]);", x, y)

            if element:
                # Elementi highlight et
                self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
                self.driver.execute_script("arguments[0].style.backgroundColor='yellow'", element)

                # Elemente tıkla
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()

                # Metni karakter karakter yaz
                for karakter in text:
                    actions = ActionChains(self.driver)
                    actions.send_keys(karakter)
                    actions.perform()
                    time.sleep(delay_ms / 1000)  # milisaniyeyi saniyeye çevir

                print(f"Metin başarıyla yazıldı: {text}")
            else:
                print(f"Koordinatlarda element bulunamadı: ({x}, {y})")

        except Exception as e:
            print(f"Hata oluştu: {str(e)}")


if __name__ == "__main__":
    driver_manager_page = DriverManagerPage()
    AB_Testing_Page = US001AB_Testing()

    # Heroku ana sayfasına git
    driver_manager_page.navigate_heroku_homePage()

    # AB Testing sayfasına git
    AB_Testing_Page.navigate_AB_Testing()

    # Alfabeyi yazdır
    # AB_Testing_Page.highlight_and_type_alphabet()

    # Alternatif: Özel bir metin yazdırmak için
    AB_Testing_Page.highlight_and_type_with_delay("Merhaba Dunya", 150)

    # 2 saniye bekle ve driver'ı kapat
    time.sleep(2)
    driver_manager_page.close_driver()



