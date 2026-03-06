*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/BrokenImagesPage.py

*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate Broken Images Page
    Find Broken Images
    Close Driver
