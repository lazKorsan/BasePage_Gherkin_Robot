*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/CheckboxesPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Checkboxes Page
    Press checkboxes with index
    Close Driver
