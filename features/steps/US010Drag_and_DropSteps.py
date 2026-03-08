
from behave import given

from pages.Drag_and_DropPage import Drag_and_DropPage

@given(u'Drag and Drop Easy Way')
def step_impl(context):
    context.page=Drag_and_DropPage()
    context.page.drag_and_drop_easy_way()


