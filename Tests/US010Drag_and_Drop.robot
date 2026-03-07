*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/Drag_and_DropPage.py

*** Test Cases ***
Drag and Drop easy way test
    [Documentation]    drag and drop testi
    [Tags]    dragDrop
    Navigate Heroku Home Page
    Drag and Drop Easy Way
    Close Driver
