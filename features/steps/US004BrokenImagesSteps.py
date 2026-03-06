from behave import given

from pages.BrokenImagesPage import BrokenImagesPage


@given(u'Navigate brokenImages Page')
def step_impl(context):
    context.brokenImagesPage = BrokenImagesPage()
    context.brokenImagesPage.navigate_broken_images()



@given(u'Find broken images')
def step_impl(context):
    context.brokenImagesPage.find_broken_images()