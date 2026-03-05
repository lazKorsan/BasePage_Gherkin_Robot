from behave import given

from pages.BasicAuthPage import BasicAuthPage


@given(u'Navigate Basic Auth Page')
def step_impl(context):
    context.basicAuthPage = BasicAuthPage()
    context.basicAuthPage.navigate_basic_auth_Page()



@given(u'Kullanici popUp menusune gecerli bilgileri girer')
def step_impl(context):
    context.basicAuthPage.user_enters_valid_info_into_popUpMenu("admin", "admin")