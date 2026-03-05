from behave import given
from pages.DriverManagerPage import DriverManagerPage

@given(u'Navigate Heroku Home Page')
def step_impl(context):
    context.driver_manager_page = DriverManagerPage()
    context.driver_manager_page.navigate_heroku_homePage()

@given(u'Close Driver')
def step_impl(context):
    context.driver_manager_page.close_driver()

