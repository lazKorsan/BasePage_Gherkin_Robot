

*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/AddRemoveElementsPage.py


*** Test Cases ***
add remove elements test US002_TC01
    [Documentation]    Basit push testi
    [Tags]    addRemoveElements
    Navigate Heroku Home Page
    Navigate Add Remove Elements Page
    Add Elements
    Delete Elements
    Close Driver