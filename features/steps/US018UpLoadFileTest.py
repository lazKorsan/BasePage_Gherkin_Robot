from behave import given

from pages.FileUploadPage import FileUploadPage


@given(u'Navigate File Upload Page')
def step_impl(context):
    context.page = FileUploadPage()
    context.page.navigate_file_upload_page()




@given(u'File Upload Process')
def step_impl(context):
    context.page.file_upload_process()



@given(u'Assert Up Load File Name')
def step_impl(context):
    context.page.assert_up_load_file_name()

