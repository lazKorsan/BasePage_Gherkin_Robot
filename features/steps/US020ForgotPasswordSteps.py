
from behave import given

from pages.ForgotPasswordPage import ForgotPasswordPage


@given(u'Navigate Password Page')
def step_impl(context):
    context.page = ForgotPasswordPage()
    context.page.click_forgot_password_link_button()


@given(u'Forgot Password Send "lazKorsan@gmail.com"')
def step_impl(context):
    context.page.send_email(userMail="lazKorsan@gmail.com")


@given(u'Click Forgot Password Button')
def step_impl(context):
    context.page.click_forgot_password()