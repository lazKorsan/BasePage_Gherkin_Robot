*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/ForgotPasswordPage.py

*** Variables ***
${userMail}    lazKorsan@gmail.com


*** Test Cases ***
us020 Forgot Password Test
    [Documentation]    assert forgot password test
    [Tags]    forgotPassword
    Navigate Heroku Home Page
    Navigate Password Page
    Forgot Password Send Mail    ${USERMAIL}
    Click Forgot Password Button
    Close Driver
