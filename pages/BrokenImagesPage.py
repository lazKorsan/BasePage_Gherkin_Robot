
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import requests
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time

from pages.DriverManagerPage import DriverManagerPage


class BrokenImagesPage(BasePage):

    brokenImagesButton = (By.XPATH, '//*[@href="/broken_images"]')
    
    # Tüm görselleri bulmak için genel bir locator kullanıyoruz
    IMAGES = (By.CSS_SELECTOR, "div.example img")

    @keyword("Navigate Broken Images Page")
    def navigate_broken_images(self):

        self.click(self.brokenImagesButton)

        time.sleep(1)

    @keyword("Find Broken Images")
    def find_broken_images(self):

        images = self.find_elements(self.IMAGES)
        broken_images = []

        print(f"Toplam {len(images)} görsel bulundu.")


        for index, img in enumerate(images, 1):
            image_url = img.get_attribute("src")

            if not image_url:
                print(f"Görsel {index}: src attribute'ü boş")
                broken_images.append({
                    'url': 'Boş src',
                    'status_code': 'N/A',
                    'index': index
                })
                continue

            print(f"Görsel {index} kontrol ediliyor: {image_url}")

            try:

                response = requests.get(image_url, timeout=10)

                if response.status_code != 200:
                    print(f"✗ Kırık görsel: {image_url} - Status code: {response.status_code}")
                    broken_images.append({
                        'url': image_url,
                        'status_code': response.status_code,
                        'index': index
                    })
                else:
                    print(f"✓ Geçerli görsel: {image_url} - Status code: {response.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"✗ Hata: {image_url} kontrol edilirken hata oluştu - {str(e)}")
                broken_images.append({
                    'url': image_url,
                    'status_code': 'Hata',
                    'error': str(e),
                    'index': index
                })


        print(f"\n=== ÖZET ===")
        print(f"Toplam görsel: {len(images)}")
        print(f"Kırık görsel sayısı: {len(broken_images)}")

        if broken_images:
            print("\nKırık görseller:")
            for broken in broken_images:
                print(f"  {broken['index']}. {broken['url']} - Status: {broken['status_code']}")

        return broken_images


def test_broken_images_tc02():
    driver_manager_page = DriverManagerPage()
    broken_images_page = BrokenImagesPage()

    driver_manager_page.navigate_heroku_homePage()
    broken_images_page.navigate_broken_images()
    broken_images_page.find_broken_images()




def test_broken_images():
    driver_manager_page = DriverManagerPage()
    broken_images_page = BrokenImagesPage()

    driver_manager_page.navigate_heroku_homePage()
    broken_images_page.navigate_broken_images()
    broken_images = broken_images_page.find_broken_images()
    if len(broken_images) > 0:
        print("\n❌ TEST FAILED: Kırık görseller bulundu!")
        return
    else:
        print("\n✅ TEST PASSED: Tüm görseller sağlam!")


    driver_manager_page.close_driver()




def test_broken_images_tc01():
    """
    Java'daki main metodunun Python karşılığı.
    Bu fonksiyonu doğrudan çalıştırabilirsiniz.
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager

    # Firefox driver'ı başlat
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Pencereyi maximize et
        driver.maximize_window()

        # URL'ye git
        driver.get("https://the-internet.herokuapp.com/")

        # BrokenImagesPage nesnesi oluştur
        broken_images_page = BrokenImagesPage()

        # Broken images sayfasına git
        broken_images_page.navigate_broken_images()

        # Kırık görselleri bul
        broken_images = broken_images_page.find_broken_images()

        # Test sonucunu kontrol et
        if len(broken_images) > 0:
            print("\n❌ TEST FAILED: Kırık görseller bulundu!")
        else:
            print("\n✅ TEST PASSED: Tüm görseller sağlam!")

    finally:
        # Tarayıcıyı kapat
        time.sleep(1)
        driver.quit()


if __name__ == "__main__":
    test_broken_images()