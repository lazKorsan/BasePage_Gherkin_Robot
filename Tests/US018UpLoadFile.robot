*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/FileUploadPage.py


*** Test Cases ***
UpLoad File test
    [Documentation]    choosefile button enter file path
    [Tags]    upLoadFile
    Navigate Heroku Home Page
    Navigate File Upload Page
    File Upload Process
    Assert Up Load File Name
    Close Driver
