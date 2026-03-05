


*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/BasicAuthPage.py

*** Variables ***
${USER_NAME}   admin
${PASSWORD}    admin

*** Test Cases ***
PopUp Menu request yapı ile giris yapma testi
    [Documentation]    Kullanici popUpMenu bilgilerini url ile girer
    [Tags]    AuthenticationPopUpUrl
    Navigate Heroku Home Page
    Navigate Basic Auth Page
    Kullanici popUp menusune gecerli bilgileri girer  ${USER_NAME}  ${PASSWORD}
    Close Driver