*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/DigestAuthenticationPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Digest Authentication Page
    Login Digest Authentication Page
    Close Driver
