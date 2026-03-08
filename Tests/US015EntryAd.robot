*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/EntryAdPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    Modal Button tiklma testi
    [Tags]    EntryAd
    Navigate Heroku Home Page
    Navigate Entry Ad Page
    Push Modal Close Button
    Close Driver
