from behave import given

from pages.ChallengingDomPage import ChallengingDomPage


@given(u'Navigate Challenging Dom Page')
def step_impl(context):
    context.challengingDomPage = ChallengingDomPage()
    context.challengingDomPage.navigate_challenging_dom()




@given(u'Description Color Button')
def step_impl(context):
    context.challengingDomPage.description_coulor_button()