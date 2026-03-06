
from behave import given

from pages.ContextMenuPage import ContextMenuPage


@given(u'Navigate Context Menu Page')
def step_impl(context):
    context.context_page = ContextMenuPage()
    context.context_page.navigate_context_menu()



@given(u'Complete Context Menu Test')
def step_impl(context):
    context.context_page.right_click_on_context_area()
    context.context_page.get_alert_text()
    context.context_page.accept_alert()
