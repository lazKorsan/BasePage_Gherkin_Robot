import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time

from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class DropdownPage(BasePage):
    # Locators
    dropDownButton = (By.XPATH, '//*[@href="/dropdown"]')
    selectElement = (By.ID, 'dropdown')  # ID kullanmak daha güvenilir

    # Farklı seçim stratejileri için locators
    option1 = (By.XPATH, '//select[@id="dropdown"]/option[@value="1"]')
    option2 = (By.XPATH, '//select[@id="dropdown"]/option[@value="2"]')

    @keyword("Navigate Dropdown Page")
    def navigate_dropdown(self):
        """Dropdown sayfasına navigate et"""
        try:
            self.click(self.dropDownButton)
            self.wait_for_page_load()
        except Exception as e:
            print(f"Navigation hatası: {e}")
            raise

    def wait_for_page_load(self, timeout=10):
        """Sayfanın yüklendiğini bekle"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.selectElement)
        )

    # METHOD 1: Select sınıfı ile profesyonel seçim
    @keyword("Select by value with Select class")
    def select_by_value_with_select_class(self, option_value="1"):
        """
        Selenium'un built-in Select sınıfını kullanarak dropdown seçimi
        En profesyonel ve güvenilir yöntem
        """
        try:
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.selectElement)
            )
            select = Select(dropdown_element)
            select.select_by_value(option_value)
            print(f"Option {option_value} value ile seçildi")
            time.sleep(1)
        except Exception as e:
            print(f"Select sınıfı ile seçim hatası: {e}")
            raise

    # METHOD 2: Görünür text ile seçim
    def select_by_visible_text(self, text="Option 1"):
        """
        Dropdown'daki görünür text'e göre seçim yapar
        Kullanıcı davranışına en yakın yöntem
        """
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.selectElement)
            )
            select = Select(dropdown)
            select.select_by_visible_text(text)
            print(f"'{text}' text'i ile seçim yapıldı")
            time.sleep(1)
        except Exception as e:
            print(f"Text ile seçim hatası: {e}")
            raise

    # METHOD 3: Index ile seçim
    def select_by_index(self, index=1):
        """
        Dropdown'daki index numarasına göre seçim (0'dan başlar)
        Dinamik dropdownlar için kullanışlı
        """
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.selectElement)
            )
            select = Select(dropdown)
            select.select_by_index(index)
            print(f"Index {index} ile seçim yapıldı")
            time.sleep(1)
        except Exception as e:
            print(f"Index ile seçim hatası: {e}")
            raise

    # METHOD 4: JavaScript ile seçim
    def select_with_javascript(self, option_value="1"):
        """
        JavaScript executor kullanarak dropdown seçimi
        Sayfa elementlerinin tıklanabilir olmadığı durumlarda kullanışlı
        """
        try:
            js_script = f"""
                var select = document.getElementById('dropdown');
                select.value = '{option_value}';
                var event = new Event('change', {{ bubbles: true }});
                select.dispatchEvent(event);
            """
            self.driver.execute_script(js_script)
            print(f"JavaScript ile option {option_value} seçildi")
            time.sleep(1)
        except Exception as e:
            print(f"JavaScript seçim hatası: {e}")
            raise

    # METHOD 5: ActionChains ile hover ve seçim simülasyonu
    def select_with_action_chains(self, option_value="1"):
        """
        Mouse hareketlerini simüle ederek dropdown seçimi
        Gerçek kullanıcı davranışına en yakın yöntem
        """
        try:
            # Dropdown'u bul ve tıkla
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.selectElement)
            )

            # ActionChains ile hover ve click simülasyonu
            actions = ActionChains(self.driver)
            actions.move_to_element(dropdown).click().perform()
            time.sleep(1)

            # Option'ı bul ve tıkla
            option_locator = (By.XPATH, f'//select[@id="dropdown"]/option[@value="{option_value}"]')
            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )

            # Option'a hover yap ve tıkla
            actions.move_to_element(option).click().perform()
            print(f"ActionChains ile option {option_value} seçildi")
            time.sleep(1)

        except Exception as e:
            print(f"ActionChains seçim hatası: {e}")
            raise

    # METHOD 6: Klavye kısayolları ile seçim
    def select_with_keyboard(self, option_index=1):
        """
        Klavye kullanarak dropdown seçimi (ok tuşları + enter)
        Erişilebilirlik testleri için ideal
        """
        try:
            # Dropdown'u focus yap
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.selectElement)
            )
            dropdown.click()
            time.sleep(1)

            # Klavye ile seçim
            actions = ActionChains(self.driver)

            # Ok tuşlarıyla istenen option'a git
            for _ in range(option_index):
                actions.send_keys('\ue015')  # DOWN arrow
                time.sleep(0.3)

            # Enter ile seçimi onayla
            actions.send_keys('\ue007').perform()
            print(f"Klavye ile option {option_index} seçildi")
            time.sleep(1)

        except Exception as e:
            print(f"Klavye seçim hatası: {e}")
            raise

    # METHOD 7: Random seçim
    def select_random_option(self):
        """
        Dropdown'dan random bir option seçer
        Edge case testleri için kullanışlı
        """
        import random

        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.selectElement)
            )
            select = Select(dropdown)

            # Tüm optionları al ve disabled olmayanları filtrele
            options = [opt for opt in select.options if not opt.is_enabled()]
            if options:
                random_option = random.choice(options)
                select.select_by_visible_text(random_option.text)
                print(f"Random seçim: {random_option.text}")
            else:
                print("Seçilebilir option bulunamadı")

            time.sleep(1)

        except Exception as e:
            print(f"Random seçim hatası: {e}")
            raise

    # Seçim doğrulama metodu
    def verify_selection(self, expected_value):
        """
        Seçilen option'ın doğruluğunu kontrol eder
        """
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.selectElement)
            )
            select = Select(dropdown)
            selected_option = select.first_selected_option

            is_correct = selected_option.get_attribute('value') == expected_value
            print(f"Seçim doğrulama: {'✓ Başarılı' if is_correct else '✗ Başarısız'}")
            print(f"Seçilen: {selected_option.text}, Beklenen value: {expected_value}")

            return is_correct

        except Exception as e:
            print(f"Doğrulama hatası: {e}")
            return False
    # todo //<!--
    # Dinamik dropdown'lar için (AJAX ile yüklenen)
    def wait_and_select_dynamic_dropdown(self, expected_text, timeout=10):
        """Dinamik olarak yüklenen dropdown için bekle ve seç"""
        try:
            # Dropdown'un yüklenmesini bekle
            dropdown = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.selectElement)
            )

            # Option'ların yüklenmesini bekle
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(Select(dropdown).options) > 1
            )

            select = Select(dropdown)
            select.select_by_visible_text(expected_text)
            print(f"✓ Dinamik dropdown'dan '{expected_text}' seçildi")

        except TimeoutException:
            print(f"✗ Dropdown yüklenemedi veya '{expected_text}' bulunamadı")

    # Çoklu seçim yapılabilen dropdown'lar için
    def select_multiple_options(self, option_values=[]):
        """Birden fazla option seçimi (multiple select için)"""
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.selectElement)
            )

            # Multiple select kontrolü
            if not dropdown.get_attribute('multiple'):
                print("Bu dropdown çoklu seçim desteklemiyor")
                return

            select = Select(dropdown)
            for value in option_values:
                select.select_by_value(value)
                print(f"✓ Option {value} seçildi")

            # Seçimleri doğrula
            selected = [opt.get_attribute('value') for opt in select.all_selected_options]
            print(f"Seçilenler: {selected}")

        except Exception as e:
            print(f"Çoklu seçim hatası: {e}")
   # todo |||| //<!--

def test_dropdown_with_multiple_methods():
    """
    Tüm dropdown seçim metodlarını test eden ana fonksiyon
    """
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dropdown_page = DropdownPage()

    # Dropdown sayfasına git
    dropdown_page.navigate_dropdown()
    print("\n=== Dropdown Test Başladı ===\n")

    # Test 1: Select sınıfı ile
    print("1. Select sınıfı ile seçim:")
    dropdown_page.select_by_value_with_select_class("1")
    dropdown_page.verify_selection("1")
    print("-" * 40)

    # Test 2: Görünür text ile
    print("2. Görünür text ile seçim:")
    dropdown_page.select_by_visible_text("Option 2")
    dropdown_page.verify_selection("2")
    print("-" * 40)

    # Test 3: Index ile
    print("3. Index ile seçim:")
    dropdown_page.select_by_index(1)  # Option 1
    dropdown_page.verify_selection("1")
    print("-" * 40)

    # Test 4: JavaScript ile
    print("4. JavaScript ile seçim:")
    dropdown_page.select_with_javascript("2")
    dropdown_page.verify_selection("2")
    print("-" * 40)

    # Test 5: ActionChains ile
    print("5. ActionChains ile seçim:")
    dropdown_page.select_with_action_chains("1")
    dropdown_page.verify_selection("1")
    print("-" * 40)

    # Test 6: Klavye ile
    print("6. Klavye ile seçim:")
    dropdown_page.select_with_keyboard(1)  # Option 1
    dropdown_page.verify_selection("1")
    print("-" * 40)

    # Test 7: Random seçim
    print("7. Random seçim:")
    dropdown_page.select_random_option()

    print("\n=== Tüm testler tamamlandı ===\n")

    # Tarayıcıyı kapat
    driver_manager.driver.quit()


# Tek bir metodla test etmek isterseniz:
def test_simple_dropdown():
    """Basit dropdown test"""
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dropdown_page = DropdownPage()

    dropdown_page.navigate_dropdown()

    # En profesyonel yöntemi kullan
    dropdown_page.select_by_value_with_select_class("1")

    # Alternatif olarak:
    # dropdown_page.select_by_visible_text("Option 2")

    driver_manager.driver.quit()