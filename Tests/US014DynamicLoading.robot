*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/DynamicLoadingPage.py

*** Test Cases ***
DynamicLoadinPage sayfasındaki 2 numarali test
    [Documentation]    Dynamic Loading dynamic wait
    [Tags]    dynamicLoading
    Navigate Heroku Home Page
    Navigate Dynamic Loading Page
    Click Example2
    Click Start for Example2
    Close Driver
