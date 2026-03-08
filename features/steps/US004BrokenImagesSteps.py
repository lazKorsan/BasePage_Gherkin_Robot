from behave import given

from pages.BrokenImagesPage import BrokenImagesPage


@given(u'Navigate brokenImages Page')
def step_impl(context):
    context.page = BrokenImagesPage()
    context.page.navigate_broken_images()



@given(u'Find broken images')
def step_impl(context):
    context.page.find_broken_images()