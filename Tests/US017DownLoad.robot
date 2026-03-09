*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/FileDownloadPage.py


*** Test Cases ***
driverManagerTest correction
    [Documentation]    navigate test
    [Tags]    correction
    Navigate Heroku Home Page
    Navigate File Download Page
    Download File
    Close Driver
