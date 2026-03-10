*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/FramesPage.py


*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate to Nested Frame Page
    Get Text from Nested Frame Left Frame
    Get Text from Nested Frame Middle Frame
    Get Text from Nested Frame Right Frame
    Get Text from Nested Frame Bottom Frame
    Close Driver
