from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class DisappearingElementsPage(BasePage):
    disappearingElementsButton = (By.XPATH, '//*[@href="/disappearing_elements"]')

    # Menü butonları için locator'lar
    HOME_BUTTON = (By.XPATH, '//ul/li/a[text()="Home"]')
    ABOUT_BUTTON = (By.XPATH, '//ul/li/a[text()="About"]')
    CONTACT_BUTTON = (By.XPATH, '//ul/li/a[text()="Contact Us"]')
    PORTFOLIO_BUTTON = (By.XPATH, '//ul/li/a[text()="Portfolio"]')
    GALLERY_BUTTON = (By.XPATH, '//ul/li/a[text()="Gallery"]')

    # Tüm menü öğeleri için genel locator
    ALL_MENU_ITEMS = (By.XPATH, '//ul/li/a')

    # Beklenen URL'ler
    EXPECTED_URLS = {
        "Home": "https://the-internet.herokuapp.com/",
        "About": "https://the-internet.herokuapp.com/about/",
        "Contact Us": "https://the-internet.herokuapp.com/contact-us/",
        "Portfolio": "https://the-internet.herokuapp.com/portfolio/",
        "Gallery": "https://the-internet.herokuapp.com/gallery/"
    }

    @keyword("Navigate Disappearing Elements Page")
    def navigate_disappearing_elements(self):
        self.click(self.disappearingElementsButton)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ALL_MENU_ITEMS)
        )

    @keyword("Get Visible Menu Buttons")
    def get_visible_menu_buttons(self):
        """Mevcut sayfada görünen tüm menü butonlarının isimlerini döndürür"""
        menu_buttons = self.find_elements(self.ALL_MENU_ITEMS)
        return [button.text for button in menu_buttons if button.text]

    @keyword("Get Menu Button Count")
    def get_menu_button_count(self):
        """Sayfada görünen buton sayısını döndürür"""
        return len(self.find_elements(self.ALL_MENU_ITEMS))

    @keyword("Click Menu Button")
    def click_menu_button(self, button_name):
        """Belirtilen isimdeki butona tıklar"""
        button_locator = (By.XPATH, f'//ul/li/a[text()="{button_name}"]')
        self.click(button_locator)

    @keyword("Verify Current URL")
    def verify_current_url(self, expected_url):
        """Mevcut URL'nin beklenen URL ile eşleştiğini kontrol eder"""
        current_url = self.driver.current_url
        if current_url != expected_url:
            raise AssertionError(f"URL uyuşmazlığı! Beklenen: {expected_url}, Mevcut: {current_url}")
        return True

    @keyword("Verify Button Navigation")
    def verify_button_navigation(self, button_name):
        """Butona tıklar ve doğru sayfaya yönlendirdiğini kontrol eder"""
        # Sayfa URL'ini kaydet
        initial_url = self.driver.current_url

        # Butona tıkla
        self.click_menu_button(button_name)

        # Yeni sayfanın yüklenmesini bekle
        WebDriverWait(self.driver, 5).until(EC.url_changes(initial_url))

        # URL'i kontrol et
        expected_url = self.EXPECTED_URLS.get(button_name)
        if not expected_url:
            raise ValueError(f"'{button_name}' için beklenen URL tanımlanmamış!")

        self.verify_current_url(expected_url)

        # Ana sayfaya geri dön
        self.driver.back()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ALL_MENU_ITEMS)
        )
        time.sleep(1)  # Sayfanın tamamen yenilenmesi için

        return True

    @keyword("Verify All Visible Buttons Navigation")
    def verify_all_visible_buttons_navigation(self):
        """Mevcut sayfada görünen TÜM butonların navigasyonunu test eder"""
        visible_buttons = self.get_visible_menu_buttons()

        if not visible_buttons:
            raise AssertionError("Sayfada hiç buton görünmüyor!")

        results = {}
        for button_name in visible_buttons:
            try:
                self.verify_button_navigation(button_name)
                results[button_name] = "PASS"
            except Exception as e:
                results[button_name] = f"FAIL: {str(e)}"
                # Hatadan sonra sayfaya geri dönmeye çalış
                self.driver.back()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.ALL_MENU_ITEMS)
                )

        return results

    @keyword("Refresh Until All Buttons Visible")
    def refresh_until_all_buttons_visible(self, max_attempts=10):
        """Tüm 5 buton görünene kadar sayfayı yeniler"""
        attempt = 0
        while attempt < max_attempts:
            self.driver.refresh()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ALL_MENU_ITEMS)
            )
            time.sleep(1)

            button_count = self.get_menu_button_count()
            if button_count == 5:
                print(f"Tüm 5 buton {attempt + 1}. denemede göründü!")
                return True

            attempt += 1

        raise AssertionError(f"{max_attempts} denemede tüm butonlar görünmedi! Son buton sayısı: {button_count}")

    @keyword("Is Button Visible")
    def is_button_visible(self, button_name):
        """Belirtilen butonun sayfada görünüp görünmediğini kontrol eder"""
        button_locator = (By.XPATH, f'//ul/li/a[text()="{button_name}"]')
        elements = self.find_elements(button_locator)
        return len(elements) > 0

    @keyword("Get Missing Buttons")
    def get_missing_buttons(self):
        """Sayfada görünmeyen butonların listesini döndürür"""
        visible_buttons = self.get_visible_menu_buttons()
        all_buttons = list(self.EXPECTED_URLS.keys())
        missing_buttons = [button for button in all_buttons if button not in visible_buttons]
        return missing_buttons

    @keyword("Verify Page Title")
    def verify_page_title(self, expected_title):
        """Sayfa başlığını kontrol eder"""
        actual_title = self.driver.title
        if actual_title != expected_title:
            raise AssertionError(f"Başlık uyuşmazlığı! Beklenen: {expected_title}, Mevcut: {actual_title}")
        return True


# ... (mevcut kodların üst kısmı aynen kalacak) ...

# ÖRNEK TEST METODU - Doğrudan çalıştırmak için
if __name__ == "__main__":
    """
    Bu test metodu, sayfadaki butonların dinamik davranışını test eder.
    Doğrudan Python ile çalıştırmak için: python pages/DisappearingElementsPage.py
    """
    import time
    from pages.DriverManagerPage import DriverManagerPage

    print("=" * 60)
    print("DİSAPPEARING ELEMENTS TESTİ BAŞLIYOR")
    print("=" * 60)

    # Driver'ı başlat ve ana sayfaya git
    driver_manager = DriverManagerPage()
    disappearing_page = DisappearingElementsPage()
    def try_cath_blok():
     try:
        # Ana sayfaya git
        print("\n📱 Ana sayfaya gidiliyor...")
        driver_manager.navigate_heroku_homePage()

        # Disappearing Elements sayfasına git
        print("🔍 Disappearing Elements sayfasına gidiliyor...")
        disappearing_page.navigate_disappearing_elements()
        time.sleep(2)

        # TEST 1: Sayfadaki butonları listele
        print("\n" + "-" * 40)
        print("TEST 1: Görünen Butonların Listesi")
        print("-" * 40)
        visible_buttons = disappearing_page.get_visible_menu_buttons()
        button_count = disappearing_page.get_menu_button_count()
        print(f"📊 Bu yüklemede {button_count} buton görünüyor:")
        for i, button in enumerate(visible_buttons, 1):
            print(f"   {i}. {button}")

        # TEST 2: Her butonun navigasyonunu test et
        print("\n" + "-" * 40)
        print("TEST 2: Buton Navigasyon Testleri")
        print("-" * 40)

        for button_name in visible_buttons:
            try:
                print(f"\n🖱️  '{button_name}' butonu test ediliyor...")

                # Butona tıkla ve yönlendirmeyi kontrol et
                disappearing_page.click_menu_button(button_name)
                time.sleep(2)

                # URL'i kontrol et
                expected_url = disappearing_page.EXPECTED_URLS[button_name]
                current_url = disappearing_page.driver.current_url

                if current_url == expected_url:
                    print(f"   ✅ BAŞARILI: Doğru URL -> {current_url}")
                else:
                    print(f"   ❌ HATA: Beklenen: {expected_url}")
                    print(f"            Gidilen: {current_url}")

                # Geri gel
                disappearing_page.driver.back()
                time.sleep(2)

            except Exception as e:
                print(f"   ❌ HATA: {str(e)}")
                # Hata durumunda geri gelmeyi dene
                disappearing_page.driver.back()
                time.sleep(2)

        # TEST 3: Eksik butonları kontrol et
        print("\n" + "-" * 40)
        print("TEST 3: Eksik Buton Kontrolü")
        print("-" * 40)
        missing_buttons = disappearing_page.get_missing_buttons()
        if missing_buttons:
            print(f"⚠️  Bu yüklemede görünmeyen butonlar: {', '.join(missing_buttons)}")
        else:
            print("✅ Tüm butonlar görünüyor!")

        # TEST 4: Sayfayı yenileyerek buton değişimini gözlemle
        print("\n" + "-" * 40)
        print("TEST 4: Sayfa Yenileme Testi (5 kez yenilenecek)")
        print("-" * 40)

        for refresh_count in range(1, 6):
            print(f"\n🔄 {refresh_count}. yenileme...")
            disappearing_page.driver.refresh()
            time.sleep(2)

            new_buttons = disappearing_page.get_visible_menu_buttons()
            new_count = len(new_buttons)
            print(f"   Görünen butonlar ({new_count} adet): {', '.join(new_buttons)}")

        # TEST 5: Belirli bir butonun varlığını kontrol et (opsiyonel)
        print("\n" + "-" * 40)
        print("TEST 5: Belirli Buton Kontrolü")
        print("-" * 40)

        test_buttons = ["Home", "About", "Gallery"]
        for button in test_buttons:
            is_visible = disappearing_page.is_button_visible(button)
            status = "✅ Görünüyor" if is_visible else "❌ Görünmüyor"
            print(f"   {button}: {status}")

        # TEST 6: Tüm butonları görme denemesi
        print("\n" + "-" * 40)
        print("TEST 6: Tüm Butonları Görme Denemesi (maksimum 10 deneme)")
        print("-" * 40)

        try:
            disappearing_page.refresh_until_all_buttons_visible(max_attempts=10)
            print("✅ Başarılı: Tüm butonlar görünür hale geldi!")
            final_buttons = disappearing_page.get_visible_menu_buttons()
            print(f"   Görünen butonlar: {', '.join(final_buttons)}")
        except AssertionError as e:
            print(f"⚠️  Uyarı: {str(e)}")

        print("\n" + "=" * 60)
        print("✅ TESTLER TAMAMLANDI!")
        print("=" * 60)

     except Exception as e:
        print(f"\n❌ KRİTİK HATA: {str(e)}")
        import traceback

        traceback.print_exc()

     finally:
        # Tarayıcıyı kapat
        print("\n🔚 Tarayıcı kapatılıyor...")
        driver_manager.close_driver()
        print("👋 Test sonlandı.")





def test_visibility_test02():
    driver_manager=DriverManagerPage()
    disappearing_page=DisappearingElementsPage()
    driver_manager.navigate_heroku_homePage()
    disappearing_page.try_cath_blok()