import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time

from robot.api.deco import keyword
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

from pages.DriverManagerPage import DriverManagerPage


class Drag_and_DropPage(BasePage):
    dragAndDropButton = (By.XPATH, '//*[@href="/drag_and_drop"]')
    columnA = (By.XPATH, '//*[@id="column-a"]')
    columnB = (By.XPATH, '//*[@id="column-b"]')
    columnAHeader = (By.XPATH, '//*[@id="column-a"]/header')
    columnBHeader = (By.XPATH, '//*[@id="column-b"]/header')

    @keyword("Navigate Drag and Drop Page")
    def navigate_drag_and_drop(self):
        self.click(self.dragAndDropButton)
        time.sleep(2)  # Sayfanın tamamen yüklenmesi için bekle

    @keyword("Get Column Headers")
    def get_column_headers(self):
        """A ve B sütunlarının başlıklarını döndürür"""
        a_header = self.driver.find_element(*self.columnA).text
        b_header = self.driver.find_element(*self.columnB).text
        return a_header, b_header

    @keyword("Drag and Drop - Method 1")
    def drag_and_drop_method1(self):
        """ActionChains ile drag and drop - Standart yöntem"""
        source = self.driver.find_element(*self.columnA)
        target = self.driver.find_element(*self.columnB)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(1)

    @keyword("Drag and Drop - Method 2")
    def drag_and_drop_method2(self):
        """Click and hold ile manuel drag and drop"""
        source = self.driver.find_element(*self.columnA)
        target = self.driver.find_element(*self.columnB)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()
        time.sleep(1)

    @keyword("Drag and Drop - Method 3")
    def drag_and_drop_method3(self):
        """JavaScript ile drag and drop (HTML5 drag and drop için)"""
        script = """
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }

            var source = arguments[0];
            var target = arguments[1];

            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);

            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent);

            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent);

            return true;
            """

        source = self.driver.find_element(*self.columnA)
        target = self.driver.find_element(*self.columnB)
        self.driver.execute_script(script, source, target)
        time.sleep(1)

    @keyword("Drag and Drop - Method 4")
    def drag_and_drop_method4(self):
        """Offset ile drag and drop (pixel bazlı)"""
        source = self.driver.find_element(*self.columnA)
        target = self.driver.find_element(*self.columnB)

        # Hedef elementin konumunu bul
        target_location = target.location

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element_with_offset(source,
                                                                   target_location['x'],
                                                                   target_location['y']).release().perform()
        time.sleep(1)

    @keyword("Verify Drag and Drop Success")
    def verify_drag_and_drop(self):
        """Drag and drop işleminin başarılı olup olmadığını kontrol eder"""
        a_header, b_header = self.get_column_headers()

        # Normalde A sütununda "A", B sütununda "B" yazar
        # Drag and drop sonrası yer değiştirmiş olmalılar
        if a_header == "B" and b_header == "A":
            print("✅ Drag and drop başarılı! Sütunlar yer değiştirdi.")
            return True
        elif a_header == "A" and b_header == "B":
            print("❌ Drag and drop başarısız! Sütunlar aynı yerde.")
            return False
        else:
            print(f"⚠️ Beklenmeyen durum: A={a_header}, B={b_header}")
            return False

    @keyword("Drag and Drop with Retry")
    def drag_and_drop_with_retry(self, max_attempts=3):
        """Başarılı olana kadar farklı metodlarla drag and drop'u dener"""

        for attempt in range(1, max_attempts + 1):
            print(f"\n🔄 Deneme {attempt}/{max_attempts}")

            # Her denemede farklı bir metod dene
            if attempt == 1:
                print("Metod 1: Standart drag and drop deneniyor...")
                self.drag_and_drop_method1()
            elif attempt == 2:
                print("Metod 2: Click and hold deneniyor...")
                self.drag_and_drop_method2()
            elif attempt == 3:
                print("Metod 3: JavaScript deneniyor...")
                self.drag_and_drop_method3()

            # Başarılı mı kontrol et
            if self.verify_drag_and_drop():
                print(f"✅ Deneme {attempt} başarılı!")
                return True

            # Başarısızsa sayfayı yenile ve tekrar dene
            if attempt < max_attempts:
                print("🔄 Sayfa yenileniyor...")
                self.driver.refresh()
                time.sleep(2)

        print("❌ Tüm denemeler başarısız!")
        return False


    @keyword("Drag and Drop Easy Way")
    def drag_and_drop_easy_way(self):

        drag_and_drop_page=Drag_and_DropPage()
        try:
            # Ana sayfaya git


            # Drag and Drop sayfasına git
            drag_and_drop_page.navigate_drag_and_drop()

            # Başlangıç durumunu göster
            print("\n📊 Başlangıç durumu:")
            a, b = drag_and_drop_page.get_column_headers()
            print(f"Sütun A: {a}, Sütun B: {b}")

            # Drag and drop işlemini dene
            print("\n🎯 Drag and drop işlemi başlatılıyor...")
            success = drag_and_drop_page.drag_and_drop_with_retry(max_attempts=3)

            # Son durumu göster
            print("\n📊 Son durum:")
            a, b = drag_and_drop_page.get_column_headers()
            print(f"Sütun A: {a}, Sütun B: {b}")

            if success:
                print("\n✅ TEST BAŞARILI!")
            else:
                print("\n❌ TEST BAŞARISIZ!")

        except Exception as e:
            print(f"\n❌ Hata oluştu: {str(e)}")
            import traceback

            traceback.print_exc()

        finally:
            # Tarayıcıyı kapat
            print("\n🔚 Tarayıcı kapatılıyor...")
            # driver_manager_page.close_driver()


def test_drag_and_drop_tc03():
    driver_manager_page = DriverManagerPage()
    drag_and_drop_page = Drag_and_DropPage()
    driver_manager_page.navigate_heroku_homePage()
    drag_and_drop_page.drag_and_drop_easy_way()
    driver_manager_page.close_driver()






if __name__ == "__main__":
    driver_manager_page = DriverManagerPage()
    drag_and_drop_page = Drag_and_DropPage()

    try:
        # Ana sayfaya git
        driver_manager_page.navigate_heroku_homePage()

        # Drag and Drop sayfasına git
        drag_and_drop_page.navigate_drag_and_drop()

        # Başlangıç durumunu göster
        print("\n📊 Başlangıç durumu:")
        a, b = drag_and_drop_page.get_column_headers()
        print(f"Sütun A: {a}, Sütun B: {b}")

        # Drag and drop işlemini dene
        print("\n🎯 Drag and drop işlemi başlatılıyor...")
        success = drag_and_drop_page.drag_and_drop_with_retry(max_attempts=3)

        # Son durumu göster
        print("\n📊 Son durum:")
        a, b = drag_and_drop_page.get_column_headers()
        print(f"Sütun A: {a}, Sütun B: {b}")

        if success:
            print("\n✅ TEST BAŞARILI!")
        else:
            print("\n❌ TEST BAŞARISIZ!")

    except Exception as e:
        print(f"\n❌ Hata oluştu: {str(e)}")
        import traceback

        traceback.print_exc()

    finally:
        # Tarayıcıyı kapat
        print("\n🔚 Tarayıcı kapatılıyor...")
        driver_manager_page.close_driver()