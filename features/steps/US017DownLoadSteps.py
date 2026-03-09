from behave import given

from pages.FileDownloadPage import FileDownloadPage


@given(u'Navigate File Download Page')
def step_impl(context):
    context.page = FileDownloadPage()
    context.page.navigate_file_download_page()



@given(u'Download File')
def step_impl(context):
    context.page.download_file()



