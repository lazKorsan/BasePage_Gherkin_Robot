*** Settings ***
Library    ../pages/DriverManagerPage.py


*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Close Driver
