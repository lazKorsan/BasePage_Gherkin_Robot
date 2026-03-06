*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/ContextMenuPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    popUpMenu den yazı çekme testi
    [Tags]    alertGetText
    Navigate Heroku Home Page
    Navigate Context Menu Page
    Right Click on Context Area
    Get Alert Text
    Accept Alert
    Dismiss Alert
    Close Driver
