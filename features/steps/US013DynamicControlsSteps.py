from behave import given

from pages.DynamicControlsPage import DynamicControlsPage


@given(u'Navigate Dynamic Controls Page')
def step_impl(context):
    context.page = DynamicControlsPage()
    context.page.navigate_dynamic_controls()



@given(u'Click Checkbox')
def step_impl(context):
    context.page.click_checkbox()




@given(u'Enabled Button')
def step_impl(context):
    context.page.enabled_button()