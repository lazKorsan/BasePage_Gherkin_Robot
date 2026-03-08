*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/ExitIntentPage.py


*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Exit Intent Page
    Action Mouse Move To Out Of The Viewport
    Wait For Flash Message To Appear
    Push Modal Close Button
    Close Driver
