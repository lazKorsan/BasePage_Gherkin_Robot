

from pages.DisappearingElementsPage import DisappearingElementsPage

if __name__ == "__main__":

    import time
    from pages.DriverManagerPage import DriverManagerPage

    print("=" * 60)
    print("DİSAPPEARING ELEMENTS TESTİ BAŞLIYOR")
    print("=" * 60)


    driver_manager = DriverManagerPage()
    disappearing_page = DisappearingElementsPage()

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










