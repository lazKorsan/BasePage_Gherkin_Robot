import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage
import time


class DynamicContentPage(BasePage):
    dynamicContentButton = (By.XPATH, '//*[@href="/dynamic_content"]')
    
    # Tüm dinamik içerik satırlarını (resim + metin) kapsayan locator
    # Genellikle id="content" altındaki "row" class'lı div'ler
    dynamicContentContainers = (By.XPATH, '//div[@id="content"]/div[@class="row"]')
    
    # "click here" linki
    clickHereLink = (By.XPATH, '//a[contains(text(),"click here")]')

    @keyword("Navigate Dynamic Content Page")
    def navigate_dynamic_content(self):
        self.click(self.dynamicContentButton)


    @keyword("Verify Dynamic Content Changed")
    def verify_dynamic_content_changed(self):
        """
        Sayfadaki dinamik içeriklerin 'click here' linkine tıklandığında değiştiğini doğrular.
        """
        
        # 1. Mevcut içerikleri al
        first_elements = self.find_elements(self.dynamicContentContainers)
        first_texts = [el.text for el in first_elements]
        
        print(f"\n--- İlk Durum ---")
        for i, text in enumerate(first_texts, 1):
            print(f"Satır {i}: {text[:50]}...") # İlk 50 karakteri yazdır

        # 2. Linke tıkla (Sayfa yenilenir/içerik değişir)
        self.click(self.clickHereLink)
        time.sleep(1) # Sayfanın yenilenmesi için kısa bir bekleme

        # 3. Yeni içerikleri al
        # Sayfa yenilendiği için elementleri tekrar bulmamız gerekir (StaleElementReferenceException önlemek için)
        second_elements = self.find_elements(self.dynamicContentContainers)
        second_texts = [el.text for el in second_elements]

        print(f"\n--- İkinci Durum ---")
        for i, text in enumerate(second_texts, 1):
            print(f"Satır {i}: {text[:50]}...")

        # 4. Karşılaştırma yap
        # En az bir satırın değişmiş olması beklenir (bazen şans eseri aynı gelebilir ama hepsi aynı gelmemeli)
        changes_count = 0
        for i in range(len(first_texts)):
            if first_texts[i] != second_texts[i]:
                changes_count += 1
                print(f"✓ Satır {i+1} değişti.")
            else:
                print(f"⚠ Satır {i+1} aynı kaldı.")

        if changes_count > 0:
            print("\n✅ TEST PASSED: İçerik değişimi doğrulandı.")
        else:
            print("\n❌ TEST FAILED: Hiçbir içerik değişmedi!")
            
        return changes_count > 0


def test_dynamic_content():
    driver_manager = DriverManagerPage()
    try:
        driver_manager.navigate_heroku_homePage()

        dynamic_content_page = DynamicContentPage()
        dynamic_content_page.navigate_dynamic_content()
        
        # Test sonucunu kontrol et
        assert dynamic_content_page.verify_dynamic_content_changed() == True
        
    finally:
        driver_manager.close_driver()

def test_dynamic_content_tc02():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    dynamic_content_page = DynamicContentPage()
    dynamic_content_page.navigate_dynamic_content()
    assert dynamic_content_page.verify_dynamic_content_changed() == True
    driver_manager.close_driver()

if __name__ == "__main__":
    test_dynamic_content()