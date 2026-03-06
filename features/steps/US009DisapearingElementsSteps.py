
from behave import given

from pages.DisappearingElementsPage import DisappearingElementsPage
from pages.DriverManagerPage import DriverManagerPage


@given(u'Disapearing Elements testi')
def step_impl(context):
    context.driver_manager = DriverManagerPage()
    context.disappearing_page = DisappearingElementsPage()
    try:
        # Ana sayfaya git ve test sayfasına yönlen
        context.driver_manager.navigate_heroku_homePage()
        context.disappearing_page.navigate_disappearing_elements()
        context.disappearing_page.verify_all_visible_buttons_navigation()
    except Exception as e:
        print(f"\n❌ Test hatası: {str(e)}")
    finally:
        context.driver_manager.close_driver()
        print("\n👋 Test tamamlandı.")

