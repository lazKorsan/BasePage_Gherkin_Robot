*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/ContextMenuPage.py
Library    ../pytestMethod/US007ContextMenu.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    popUpMenu den yazı çekme testi
    [Tags]    alertGetText
    Navigate Heroku Home Page
    Multi Method
    Close Driver
