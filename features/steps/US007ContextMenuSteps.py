
from behave import given

from pages.ContextMenuPage import ContextMenuPage


@given(u'Navigate Context Menu Page')
def step_impl(context):
    context.page = ContextMenuPage()
    context.page.navigate_context_menu()



@given(u'Complete Context Menu Test')
def step_impl(context):
    context.page.right_click_on_context_area()
    context.page.get_alert_text()
    context.page.accept_alert()
