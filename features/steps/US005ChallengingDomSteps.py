from behave import given

from pages.ChallengingDomPage import ChallengingDomPage


@given(u'Navigate Challenging Dom Page')
def step_impl(context):
    context.page = ChallengingDomPage()
    context.page.navigate_challenging_dom()




@given(u'Description Color Button')
def step_impl(context):
    context.page.description_coulor_button()