import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from robot.api.deco import keyword

from pages.BasePage import BasePage
from pages.DisappearingElementsPage import DisappearingElementsPage
from pages.DriverManagerPage import DriverManagerPage

class US009DisapperingElementsPreCondition09(BasePage):

    @keyword("sahis disaapearing elements testi yapardirmisitrmistir")
    def disappearing_elements(self):
     driver_manager = DriverManagerPage()
     disappearing_page = DisappearingElementsPage()

     try:
    # Ana sayfaya git ve test sayfasına yönlen
       driver_manager.navigate_heroku_homePage()
       disappearing_page.navigate_disappearing_elements()
       disappearing_page.verify_all_visible_buttons_navigation()
     except Exception as e:
      print(f"\n❌ Test hatası: {str(e)}")
     finally:
      driver_manager.close_driver()
      print("\n👋 Test tamamlandı.")

if __name__ == "__main__":
     US009DisapperingElementsPreCondition09()