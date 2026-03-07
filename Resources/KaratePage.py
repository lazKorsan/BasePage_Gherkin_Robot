import time

from pages.BasePage import BasePage
from pages.DriverManagerPage import DriverManagerPage


class KaretePage(BasePage):
    karete_url="https://karatelabs.github.io/karate/"
    dequen_url="https://dequeuniversity.com/demo/dream#"
    dequen_home_url="https://dequeuniversity.com/"
    driver_manager_page= DriverManagerPage()
    def navigate_karete_home_page(self):
        self.get_url(self.karete_url)

        # https://dequeuniversity.com/demo/dream#
        # https://dequeuniversity.com/


def test_naivegatter_karete_homenyare_pageinyare():
    driver_manager_page=DriverManagerPage()
    karete_page=KaretePage()
    karete_page.navigate_karete_home_page()
    time.sleep(2300)