from behave import given

from pages.DynamicLoadingPage import DynamicLoadingPage


@given(u'Navigate Dynamic Loading Page')
def step_impl(context):
    context.page = DynamicLoadingPage()
    context.page.navigate_dynamic_loading()



@given(u'Click Example1')
def step_impl(context):
    context.page.click_example1()



@given(u'Click Start for Example1')
def step_impl(context):
    context.page.click_start_for_example1()




