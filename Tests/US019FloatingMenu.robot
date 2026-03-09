*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/FloatingMenuPage.py


*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Folating Menu Page
    Scroll to Given Numbers of Object Text
    Definition one Of Menu Button spacially Home Buttonare
    Close Driver
