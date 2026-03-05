


*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/FormAuthenticationPage.py

*** Variables ***
${USER_NAME}    user
${PASSWORD}    pass!
*** Test Cases ***
Coklu Sayfa Denemesi
    [Documentation]    iki farkli siniftan import cekme denemesi
    [Tags]    multiPage
    Navigate Heroku Home Page
    Navigate Form Authentication Page
    User logs in with valid credentials  ${USER_NAME}  ${PASSWORD}
    Close Driver