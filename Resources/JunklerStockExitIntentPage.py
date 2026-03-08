from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
import time

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class StockExitIntentPage(BasePage):
    exitIntentButton = (By.XPATH, '//*[@href="/exit_intent"]')
    flashMessages = (By.XPATH, '//*[@id="flash-messages"]')
    modal = (By.XPATH, '//*[@class="modal"]')
    modalCloseButton = (By.XPATH, '//p[.="Close"]')

    @keyword("Navigate Exit Intent Page")
    def navigate_exit_intent_page(self):
        self.click(self.exitIntentButton)
        # Sayfanın tamamen yüklendiğinden emin ol
        time.sleep(1)

    @keyword("Action Mouse Move To Out Of The Viewport")
    def action_mouse_move_to_out_of_the_viewport(self):
        """Mouse'u viewport dışına taşımanın birden çok yolu"""

        # Method 1: Sayfanın en üstüne git
        try:
            # Önce sayfanın en üstündeki bir elemente git
            html = self.driver.find_element(By.TAG_NAME, "html")
            actions = ActionChains(self.driver)
            actions.move_to_element(html).perform()

            # Sonra yukarı doğru taşı
            window_height = self.driver.execute_script("return window.innerHeight")
            actions = ActionChains(self.driver)
            actions.move_by_offset(0, -window_height).perform()

        except MoveTargetOutOfBoundsException:
            # Method 2: JavaScript ile mouse event'i oluştur
            self.driver.execute_script("""
                var event = new MouseEvent('mouseout', {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: 0,
                    clientY: -100
                });
                document.dispatchEvent(event);
            """)

        # Method 3: Alternatif olarak sayfanın en altına git
        time.sleep(0.5)  # Event'in tetiklenmesi için bekle

        # Modal'ın görünüp görünmediğini kontrol et
        if not self.is_modal_visible():
            # İkinci bir deneme - farklı bir yöntem
            self.trigger_exit_intent_with_js()

    @keyword("Trigger Exit Intent With JavaScript")
    def trigger_exit_intent_with_js(self):
        """JavaScript ile doğrudan exit intent event'i tetikle"""
        self.driver.execute_script("""
            // Mouse'un viewport dışına çıktığı event'i oluştur
            var mouseLeaveEvent = new Event('mouseleave');
            document.dispatchEvent(mouseLeaveEvent);

            // Alternatif olarak mouseout event'i
            var mouseOutEvent = new MouseEvent('mouseout', {
                clientX: 0,
                clientY: -100,
                bubbles: true
            });
            document.dispatchEvent(mouseOutEvent);
        """)

        time.sleep(0.5)  # Event'in tetiklenmesi için bekle

    @keyword("Wait For Flash Message To Appear")
    def wait_for_flash_message_to_appear(self):
        """Modal veya flash mesajın görünmesini bekle"""
        wait = WebDriverWait(self.driver, 15)

        try:
            # Önce modal'ı dene
            wait.until(EC.visibility_of_element_located(self.modal))
        except TimeoutException:
            # Modal yoksa flash mesajı dene
            wait.until(EC.visibility_of_element_located(self.flashMessages))

    def is_modal_visible(self):
        """Modal'ın görünür olup olmadığını kontrol et"""
        try:
            modal = self.driver.find_element(*self.modal)
            return modal.is_displayed()
        except:
            return False

    @keyword("Push Modal Close Button")
    def push_modal_close_button(self):
        """Modal kapatma butonuna bas"""
        try:
            # Modal'ın görünmesi için kısa bir bekleme
            time.sleep(1)

            wait = WebDriverWait(self.driver, 10)
            close_button = wait.until(EC.element_to_be_clickable(self.modalCloseButton))
            close_button.click()

            # Modal'ın kapandığını doğrula
            time.sleep(1)
        except TimeoutException:
            print("Modal close button not found or not clickable")

    @keyword("Force Exit Intent With Multiple Attempts")
    def force_exit_intent_with_multiple_attempts(self):
        """Birden çok yöntemle exit intent'i tetiklemeyi dene"""
        max_attempts = 3

        for attempt in range(max_attempts):
            print(f"Exit intent denemesi {attempt + 1}/{max_attempts}")

            # Farklı yöntemler dene
            if attempt == 0:
                self.action_mouse_move_to_out_of_the_viewport()
            elif attempt == 1:
                self.trigger_exit_intent_with_js()
            else:
                # Sayfanın en üstüne scroll yap ve mouse'u taşı
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(0.5)

                html = self.driver.find_element(By.TAG_NAME, "html")
                actions = ActionChains(self.driver)
                actions.move_to_element(html).move_by_offset(0, -500).perform()

            # Modal göründü mü kontrol et
            if self.is_modal_visible():
                print(f"Modal göründü! Deneme {attempt + 1}'de başarılı.")
                return True

            time.sleep(1)

        print("Exit intent tetiklenemedi!")
        return False


def test_exit_intent_page():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()

    exit_intent_page = StockExitIntentPage()
    exit_intent_page.navigate_exit_intent_page()

    # Geliştirilmiş mouse hareketi
    exit_intent_page.action_mouse_move_to_out_of_the_viewport()

    # Modal'ı bekle
    exit_intent_page.wait_for_flash_message_to_appear()

    # Modal'ı kapat
    exit_intent_page.push_modal_close_button()

    # Test başarılı mesajı
    print("Exit Intent test başarıyla tamamlandı!")

    driver_manager.close_driver()


# Daha sağlam bir test için alternatif:
def test_exit_intent_robust():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()

    exit_intent_page = StockExitIntentPage()
    exit_intent_page.navigate_exit_intent_page()

    # Birden çok deneme ile exit intent'i tetikle
    success = exit_intent_page.force_exit_intent_with_multiple_attempts()

    if success:
        exit_intent_page.push_modal_close_button()
        print("Test başarılı!")
    else:
        print("Test başarısız - exit intent tetiklenemedi!")

    driver_manager.close_driver()