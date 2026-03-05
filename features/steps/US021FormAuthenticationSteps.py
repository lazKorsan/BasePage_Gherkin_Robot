from behave import given

from pages.FormAuthenticationPage import FormAuthenticationPage


@given(u'Navigate Form Authentication Page')
def step_impl(context):
    context.formAuthenticationPage = FormAuthenticationPage()
    context.formAuthenticationPage.navigate_formAuthentication_Page()



@given(u'User logs in with valid credentials')
def step_impl(context):
    context.formAuthenticationPage.user_logs_in_with_valid_credentials("user", "pass!")