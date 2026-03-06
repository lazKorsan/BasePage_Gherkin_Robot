import time

from pages.DisappearingElementsPage import DisappearingElementsPage
from pages.DriverManagerPage import DriverManagerPage


def disappearing_elements_tests_method():
    """Disappearing Elements sayfasının temel testlerini çalıştırır"""

    # Driver'ı başlat ve sayfaya git
    driver_manager = DriverManagerPage()
    disappearing_page = DisappearingElementsPage()

    try:
        # Ana sayfaya git ve test sayfasına yönlen
        driver_manager.navigate_heroku_homePage()
        disappearing_page.navigate_disappearing_elements()

        # TEST 1: Görünen butonları listele
        visible_buttons = disappearing_page.get_visible_menu_buttons()
        print(f"\n📊 Görünen butonlar ({len(visible_buttons)} adet): {', '.join(visible_buttons)}")

        # TEST 2: Her butonun navigasyonunu test et
        print("\n🖱️  Buton navigasyon testleri:")
        for button in visible_buttons:
            try:
                disappearing_page.verify_button_navigation(button)
                print(f"  ✅ {button}: Başarılı")
            except Exception as e:
                print(f"  ❌ {button}: {str(e)}")

        # TEST 3: Eksik butonları kontrol et
        missing_buttons = disappearing_page.get_missing_buttons()
        if missing_buttons:
            print(f"\n⚠️  Eksik butonlar: {', '.join(missing_buttons)}")
        else:
            print("\n✅ Tüm butonlar görünüyor!")

        # TEST 4: Sayfa yenileme testi
        print("\n🔄 Sayfa yenileme testleri:")
        for i in range(3):
            disappearing_page.driver.refresh()
            time.sleep(1)
            current_buttons = disappearing_page.get_visible_menu_buttons()
            print(f"  {i + 1}. yenileme: {len(current_buttons)} buton - {', '.join(current_buttons)}")

    except Exception as e:
        print(f"\n❌ Test hatası: {str(e)}")
    finally:
        driver_manager.close_driver()
        print("\n👋 Test tamamlandı.")

if __name__ == "__main__":
    disappearing_elements_tests_method()