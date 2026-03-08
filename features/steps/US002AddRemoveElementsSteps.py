
from behave import given
from pages.AddRemoveElementsPage import AddRemoveElementsPage


@given(u'Navigate Add Remove Elements Page')
def step_impl(context):
    context.page = AddRemoveElementsPage()
    context.page.navigate_addRemoveElements()

@given(u'Add Elements')
def step_impl(context):
    context.page.add_elements()

@given(u'Delete Elements')
def step_impl(context):
    context.page.delete_elements()

