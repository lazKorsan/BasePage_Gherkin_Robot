import time

from behave import given

from pages.DigestAuthenticationPage import DigestAuthenticationPage


@given(u'Navigate Digest Authentication Page')
def step_impl(context):
    context.page = DigestAuthenticationPage()
    context.page.navigate_digest_authentication()





@given(u'Login Digest Authentication Page')
def step_impl(context):
    context.page.sendKeys_diget_authentication()

