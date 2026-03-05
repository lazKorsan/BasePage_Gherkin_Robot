*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/AB_TestingPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate AB Testing
    Highlight and type alphabet
    Close Driver
