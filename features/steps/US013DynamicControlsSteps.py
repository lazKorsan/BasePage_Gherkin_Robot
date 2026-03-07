from behave import given

from pages.DynamicControlsPage import DynamicControlsPage


@given(u'Navigate Dynamic Controls Page')
def step_impl(context):
    context.dynamic_controls_page = DynamicControlsPage()
    context.dynamic_controls_page.navigate_dynamic_controls()



@given(u'Click Checkbox')
def step_impl(context):
    context.dynamic_controls_page.click_checkbox()




@given(u'Enabled Button')
def step_impl(context):
    context.dynamic_controls_page.enabled_button()