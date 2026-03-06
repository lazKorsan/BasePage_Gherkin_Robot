# ContextMenuPage
# C:\Users\user\PycharmProjects\use_BasePage\pages\ContextMenuPage.py
# ContextMenuPage.py
# C:\Users\user\PycharmProjects\use_BasePage\pages\ContextMenuPage.py
import sys
import os

from pages.DriverManagerPage import DriverManagerPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from pages.BasePage import BasePage
import time


class ContextMenuPage(BasePage):
    contextMenuButton = (By.XPATH, '//*[@href="/context_menu"]')
    contextContainer = (By.XPATH, '//*[@id="hot-spot"]')

    @keyword("Navigate Context Menu Page")
    def navigate_context_menu(self):
        """Context Menu sayfasına gider"""
        self.click(self.contextMenuButton)
        # Sayfanın yüklenmesi için bekle
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.contextContainer)
        )
        print("Context Menu sayfasına başarıyla gidildi.")

    @keyword("Right Click on Context Area")
    def right_click_on_context_area(self):
        """
        Belirtilen alana (hot-spot) sağ tıklar.
        Java'daki Actions class'ının Python karşılığıdır.
        """
        try:
            # Öğenin görünür olmasını bekle
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.contextContainer)
            )

            # 1. Yöntem: ActionChains ile (en yaygın)
            from selenium.webdriver.common.action_chains import ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).context_click().perform()
            print("Başarıyla sağ tık yapıldı.")

            # Alternatif 2. Yöntem: ActionBuilder ile (daha yeni ve esnek)
            # action = ActionBuilder(self.driver)
            # action.pointer_action.move_to(element).pointer_down(MouseButton.BACK).pointer_up(MouseButton.BACK)
            # action.perform()

            # Popup'ın gelmesi için kısa bir bekleme
            time.sleep(1)

        except Exception as e:
            print(f"Sağ tık işlemi sırasında hata oluştu: {str(e)}")
            raise

    @keyword("Get Alert Text")
    def get_alert_text(self):
        """
        Açılan popup (JavaScript alert) metnini alır ve konsola yazdırır.

        Returns:
            str: Alert metni
        """
        try:
            # Alert'ün görünmesini bekle (max 5 saniye)
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())

            # Alert metnini al
            alert_text = alert.text
            print(f"\n=== POPUP MESAJI ===")
            print(f"Alert metni: '{alert_text}'")
            print("====================\n")

            return alert_text

        except TimeoutException:
            print("Alert bulunamadı! Sayfada açılan bir popup yok.")
            return None
        except NoAlertPresentException:
            print("Alert bulunamadı!")
            return None
        except Exception as e:
            print(f"Alert alınırken hata oluştu: {str(e)}")
            return None

    @keyword("Accept Alert")
    def accept_alert(self):
        """
        Açık olan alert'ü kabul eder (OK butonuna basar)
        """
        try:
            alert = self.driver.switch_to.alert
            print("Alert kabul ediliyor (OK butonuna basılıyor)...")
            alert.accept()
            print("Alert başarıyla kabul edildi.")

        except NoAlertPresentException:
            print("Kabul edilecek bir alert bulunamadı!")
        except Exception as e:
            print(f"Alert kabul edilirken hata oluştu: {str(e)}")

    @keyword("Dismiss Alert")
    def dismiss_alert(self):
        """
        Açık olan alert'ü reddeder (Cancel butonuna basar)
        """
        try:
            alert = self.driver.switch_to.alert
            print("Alert reddediliyor (Cancel butonuna basılıyor)...")
            alert.dismiss()
            print("Alert başarıyla reddedildi.")

        except NoAlertPresentException:
            print("Reddedilecek bir alert bulunamadı!")
        except Exception as e:
            print(f"Alert reddedilirken hata oluştu: {str(e)}")

    @keyword("Complete Context Menu Test")
    def complete_context_menu_test(self):
        """
        Context menu testini baştan sona tek bir keyword ile yapar:
        1. Sayfaya gider
        2. Sağ tıklar
        3. Alert metnini alır ve yazdırır
        4. Alert'ü kabul eder
        """
        print("\n=== CONTEXT MENU TESTİ BAŞLIYOR ===")

        # Sayfaya git
        self.navigate_context_menu()

        # Sağ tık yap
        self.right_click_on_context_area()

        # Alert metnini al ve yazdır
        alert_text = self.get_alert_text()

        # Alert'ü kabul et
        self.accept_alert()

        print("=== CONTEXT MENU TESTİ TAMAMLANDI ===\n")

        return alert_text




# Bağımsız test fonksiyonu
def test_context_menu():
    """
    Context menu testini çalıştırmak için bağımsız fonksiyon.
    Java'daki main metodunun Python karşılığı.
    """
    from pages.DriverManagerPage import DriverManagerPage

    print("\n🚀 Context Menu Testi başlatılıyor...")

    # Sayfa nesnelerini oluştur
    driver_manager = DriverManagerPage()
    context_page = ContextMenuPage()

    try:
        # Heroku ana sayfasına git
        driver_manager.navigate_heroku_homePage()
        print("✅ Ana sayfaya gidildi.")

        # Testi komple çalıştır
        context_page.complete_context_menu_test()

        print("✅ Test başarıyla tamamlandı!")

    except Exception as e:
        print(f"❌ Test sırasında hata oluştu: {str(e)}")

    finally:
        # Driver'ı kapat
        print("🔚 Driver kapatılıyor...")
        driver_manager.close_driver()


# Eğer bu dosya doğrudan çalıştırılırsa
if __name__ == "__main__":
    test_context_menu()





