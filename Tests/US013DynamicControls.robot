*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/DynamicControlsPage.py

*** Test Cases ***
DynamicControls for wait changing elements
    [Documentation]    Dynamic Controls Elements Test
    [Tags]    DynamicControls
    Navigate Heroku Home Page
    Navigate Dynamic Controls Page
    Click Checkbox
    Enabled Button
    Close Driver
