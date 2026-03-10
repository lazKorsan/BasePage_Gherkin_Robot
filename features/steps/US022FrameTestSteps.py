from behave import given

from pages.FramesPage import FramesPage


@given(u'Navigate to Nested Frame Page')
def step_impl(context):
    context.page = FramesPage()
    context.page.navigate_to_nested_frame_page()



@given(u'Get Text from Nested Frame Left Frame')
def step_impl(context):
    context.page.get_text_left_frame()



@given(u'Get Text from Nested Frame Middle Frame')
def step_impl(context):
    context.page.get_text_middle_frame()



@given(u'Get Text from Nested Frame Right Frame')
def step_impl(context):
    context.page.get_text_right_frame()



@given(u'Get Text from Nested Frame Bottom Frame')
def step_impl(context):
    context.page.get_text_bottom_frame()

