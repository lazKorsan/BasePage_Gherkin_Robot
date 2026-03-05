
from behave import given
from pages.AddRemoveElementsPage import AddRemoveElementsPage


@given(u'Navigate Add Remove Elements Page')
def step_impl(context):
    context.addRemoveElementsPage = AddRemoveElementsPage()
    context.addRemoveElementsPage.navigate_addRemoveElements()

@given(u'Add Elements')
def step_impl(context):
    context.addRemoveElementsPage.add_elements()

@given(u'Delete Elements')
def step_impl(context):
    context.addRemoveElementsPage.delete_elements()

