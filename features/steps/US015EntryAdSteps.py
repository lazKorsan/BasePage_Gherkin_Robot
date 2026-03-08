from behave import given

from pages.EntryAdPage import EntryAdPage


@given(u'Navigate Entry Ad Page')
def step_impl(context):
    context.entry_ad_page = EntryAdPage()
    context.entry_ad_page.navigate_entry_ad_page()



@given(u'Push Modal Close Button')
def step_impl(context):
    context.entry_ad_page.push_modal_close_button()