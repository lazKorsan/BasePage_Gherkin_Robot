from behave import given

from pages.EntryAdPage import EntryAdPage


@given(u'Navigate Entry Ad Page')
def step_impl(context):
    context.page = EntryAdPage()
    context.page.navigate_entry_ad_page()
