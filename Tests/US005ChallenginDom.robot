



*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/ChallengingDomPage.py

*** Test Cases ***
driverManagerTest correction
herokuApp challenginDom test
    [Documentation]    challengingDom test
    [Tags]    challengingDom
    Navigate Heroku Home Page
    Navigate Challenging Dom Page
    Description Color Button
    Close Driver
