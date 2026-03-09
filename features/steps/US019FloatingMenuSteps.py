
from behave import given

from pages.FloatingMenuPage import FloatingMenuPage


@given(u'Navigate Folating Menu Page')
def step_impl(context):
    context.page=FloatingMenuPage()
    context.page.navigate_floating_menu_page()


@given(u'Scroll to Given Numbers of Object Text')
def step_impl(context):
    context.page.scroll_to_object_text_nd()



@given(u'Definition one Of Menu Button spacially Home Buttonare')
def step_impl(context):
    context.page.home_button_description_and_click()