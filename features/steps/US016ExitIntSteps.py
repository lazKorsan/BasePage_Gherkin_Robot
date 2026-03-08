from behave import given

from pages.ExitIntentPage import ExitIntentPage


@given(u'Navigate Exit Intent Page')
def step_impl(context):
    context.page = ExitIntentPage()
    context.page.navigate_exit_intent_page()


@given(u'Action Mouse Move To Out Of The Viewport')
def step_impl(context):
    context.page.action_mouse_move_to_out_of_the_viewport()


@given(u'Wait For Flash Message To Appear')
def step_impl(context):
    context.page.wait_for_flash_message_to_appear()
