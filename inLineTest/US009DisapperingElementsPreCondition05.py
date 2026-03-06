from pages.DisappearingElementsPage import DisappearingElementsPage
from pages.DriverManagerPage import DriverManagerPage


def disappearing_elements_tests_method():
    """Disappearing Elements sayfasının basit testi"""

    driver_manager = DriverManagerPage()
    disappearing_page = DisappearingElementsPage()

    try:
        # Sayfaya git
        driver_manager.navigate_heroku_homePage()
        disappearing_page.navigate_disappearing_elements()

        # Görünen butonları kontrol et
        buttons = disappearing_page.get_visible_menu_buttons()
        print(f"Butonlar ({len(buttons)}): {', '.join(buttons)}")

        # Her butonu test et
        for button in buttons:
            disappearing_page.verify_button_navigation(button)
            print(f"✓ {button} test edildi")

    finally:
        driver_manager.close_driver()

if __name__ == "__main__":
    disappearing_elements_tests_method()