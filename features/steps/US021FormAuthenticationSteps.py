from behave import given

from pages.FormAuthenticationPage import FormAuthenticationPage


@given(u'Navigate Form Authentication Page')
def step_impl(context):
    context.page = FormAuthenticationPage()
    context.page.navigate_formAuthentication_Page()



@given(u'User logs in with valid credentials')
def step_impl(context):
    context.page.user_logs_in_with_valid_credentials("user", "pass!")