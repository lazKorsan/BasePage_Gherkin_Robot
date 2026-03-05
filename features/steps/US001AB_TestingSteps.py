from behave import given
from pages.AB_TestingPage import AB_TestingPage


@given(u'Navigate AB Testing')
def step_impl(context):
    context.AB_testing_page = AB_TestingPage
    context.AB_testin_page.navigate_AB_Testing()

@given(u'Highlight and type alphabet')
def step_impl(context):
    context.AB_testin_page.highlight_and_type_alphabet()
