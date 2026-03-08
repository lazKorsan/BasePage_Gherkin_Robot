from behave import given
from pages.DriverManagerPage import DriverManagerPage

@given(u'Navigate Heroku Home Page')
def step_impl(context):
    context.driver_manager_page = DriverManagerPage()
    context.driver_manager_page.navigate_heroku_homePage()

@given(u'Close Driver')
def step_impl(context):
    context.driver_manager_page.close_driver()

@given(u'Push Modal Close Button')
def step_impl(context):
    # Bu adım artık context.page'in var olduğunu ve
    # üzerinde push_modal_close_button metodunun bulunduğunu varsayar.
    # Eğer bulunamazsa, AttributeError fırlatacaktır, bu da testin
    # neden başarısız olduğunu net bir şekilde gösterir.
    context.page.push_modal_close_button()
