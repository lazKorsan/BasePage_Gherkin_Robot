import time

from behave import given

from pages.DigestAuthenticationPage import DigestAuthenticationPage


@given(u'Navigate Digest Authentication Page')
def step_impl(context):
    context.digest_authentication_page = DigestAuthenticationPage()
    context.digest_authentication_page.navigate_digest_authentication()





@given(u'Login Digest Authentication Page')
def step_impl(context):
    context.digest_authentication_page.sendKeys_diget_authentication()

