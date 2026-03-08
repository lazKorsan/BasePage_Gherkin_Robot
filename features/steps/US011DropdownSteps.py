from behave import given

from pages.DropdownPage import DropdownPage


@given(u'Navigate Dropdown Page')
def step_impl(context):
    context.page = DropdownPage()
    context.page.navigate_dropdown()



@given(u'Select by value with Select class')
def step_impl(context):
    context.page.select_by_value_with_select_class("1")