import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from robot.api.deco import keyword
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class CheckboxesPage(BasePage):
    checkboxButton=(By.XPATH,'//*[@href="/checkboxes"]')
    checkBox=(By.XPATH,'//*[@type="checkbox"]')


    @keyword("Navigate Checkboxes Page")
    def navigate_checkboxes(self):
        self.click(self.checkboxButton)
    @keyword("Press in order checkboxes")
    def press_in_order_checkboxes(self):
        checkboxes = self.find_elements(self.checkBox)
        print(f"Toplam {len(checkboxes)} checkbox bulundu.")
        for index, checkbox in enumerate(checkboxes, 1):

            before_click = checkbox.is_selected()
            print(f"Checkbox {index} - Tıklama öncesi: {'Seçili' if before_click else 'Seçili değil'}")

            # Checkbox'a tıkla
            checkbox.click()

            # Tıklamadan sonraki durumu kontrol et
            after_click = checkbox.is_selected()
            print(f"Checkbox {index} - Tıklama sonrası: {'Seçili' if after_click else 'Seçili değil'}")

            # Durumun değiştiğini doğrula
            assert before_click != after_click, f"Checkbox {index} durumu değişmedi!"

            # Checkbox'lar arasında küçük bir bekleme (opsiyonel)
            self.driver.implicitly_wait(0.5)

        print("Tüm checkbox'lara başarıyla sırayla basıldı.")

    @keyword("Press checkboxes with index")
    def press_checkboxes_with_index(self, indices=None):
        """
        Belirtilen index'lerdeki checkbox'lara sırayla basar

        Args:
            indices: Tıklanacak checkbox index'leri (list, tuple veya string)
                    Örnek: [1,2] veya "1,2"
        """
        if indices is None:
            indices = [1, 2]  # Varsayılan olarak tüm checkbox'lar

        # Eğer string olarak geldiyse listeye çevir
        if isinstance(indices, str):
            indices = [int(i.strip()) for i in indices.split(',')]

        checkboxes = self.find_elements(self.checkBox)

        for idx in indices:
            if 1 <= idx <= len(checkboxes):
                checkbox = checkboxes[idx - 1]  # 0-based index'e çevir
                before_click = checkbox.is_selected()
                print(f"Checkbox {idx} - Tıklama öncesi: {'Seçili' if before_click else 'Seçili değil'}")

                checkbox.click()

                after_click = checkbox.is_selected()
                print(f"Checkbox {idx} - Tıklama sonrası: {'Seçili' if after_click else 'Seçili değil'}")
            else:
                print(f"Uyarı: {idx} numaralı checkbox bulunamadı!")

    @keyword("Verify checkboxes state")
    def verify_checkboxes_state(self, expected_states):
        """
        Checkbox'ların durumunu doğrular

        Args:
            expected_states: Beklenen durumlar listesi (True/False)
                            Örnek: [True, False] (ilk checkbox seçili, ikincisi seçili değil)
        """
        checkboxes = self.find_elements(self.checkBox)

        for i, (checkbox, expected) in enumerate(zip(checkboxes, expected_states), 1):
            actual_state = checkbox.is_selected()
            assert actual_state == expected, f"Checkbox {i} durumu uyuşmuyor! Beklenen: {expected}, Gerçek: {actual_state}"
            print(f"Checkbox {i} doğrulandı: {'Seçili' if actual_state else 'Seçili değil'}")

    @keyword("Press checkboxes alternately")
    def press_checkboxes_alternately(self, press_count=2):
        """
        Checkbox'lara alternatif olarak basar (1-2-1-2-...)

        Args:
            press_count: Toplam tıklama sayısı
        """
        checkboxes = self.find_elements(self.checkBox)

        for i in range(press_count):
            checkbox_index = i % len(checkboxes)  # 0,1,0,1,... şeklinde gider
            checkbox = checkboxes[checkbox_index]

            print(f"Tıklama {i + 1}: Checkbox {checkbox_index + 1}'a basılıyor...")
            checkbox.click()

            # Küçük bir bekleme
            self.driver.implicitly_wait(0.3)


# Test fonksiyonu
def test_checkboxes_press_in_order_test():
    """Checkbox testlerini çalıştırır"""
    driver_manager_page = DriverManagerPage()
    checkboxes_page = CheckboxesPage()

    try:
        # Ana sayfaya git
        driver_manager_page.navigate_heroku_homePage()

        # Checkboxes sayfasına git
        checkboxes_page.navigate_checkboxes()

        # Test 1: Sırayla checkbox'lara bas
        print("\n=== TEST 1: Sırayla checkbox'lara basma ===")
        checkboxes_page.press_in_order_checkboxes()

        # Test 2: Index'e göre checkbox'lara bas (opsiyonel)
        print("\n=== TEST 2: Index'e göre checkbox'lara basma ===")
        checkboxes_page.press_checkboxes_with_index([1, 2])

        # Test 3: Alternatif checkbox testi (opsiyonel)
        print("\n=== TEST 3: Alternatif checkbox testi ===")
        checkboxes_page.press_checkboxes_alternately(4)

    finally:
        # Driver'ı kapat
        driver_manager_page.close_driver()


if __name__ == "__main__":
    test_checkboxes_press_in_order_test()




def test_checboxes_press_in_order_test():
    driver_manager_page = DriverManagerPage()
    checkboxes=CheckboxesPage()
    driver_manager_page.navigate_heroku_homePage()
    checkboxes.navigate_checkboxes()
    checkboxes.press_in_order_checkboxes()
    driver_manager_page.close_driver()
