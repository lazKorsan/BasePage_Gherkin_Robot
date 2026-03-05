from pages.BrokenImagesPage import BrokenImagesPage
from pages.DriverManagerPage import DriverManagerPage


def test_broken_images():
    driver_manager_page = DriverManagerPage()
    broken_images_page = BrokenImagesPage()
    try:
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

    finally:
        driver_manager_page.close_driver()
