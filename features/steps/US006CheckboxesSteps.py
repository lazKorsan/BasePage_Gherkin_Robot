from behave import given

from pages.CheckboxesPage import CheckboxesPage


@given(u'Navigate Checkboxes Page')
def step_impl(context):
    context.checkboxesPage = CheckboxesPage()
    context.checkboxesPage.navigate_checkboxes()



@given(u'Press checkboxes with index')
def step_impl(context):
    context.checkboxesPage.press_checkboxes_with_index([1, 2])