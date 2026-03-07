*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/DropdownPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Dropdown Page
    Select by value with Select class
    Close Driver
