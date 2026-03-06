import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot.api.deco import keyword

from pages.ContextMenuPage import ContextMenuPage


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

@keyword("Multi Method")
def multi_method():
    context_page=ContextMenuPage()
    context_page.navigate_context_menu()
    context_page.right_click_on_context_area()
    context_page.get_alert_text()
    context_page.accept_alert()

