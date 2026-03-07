*** Settings ***
Library    ../pages/DriverManagerPage.py
Library    ../pages/DynamicContentPage.py
Library    BuiltIn

*** Test Cases ***
US012_TC01 DynamicContent testi
    [Documentation]    sayfada clickhere butona basıldığında icerigin degistigi dogrulanır
    [Tags]    DynamicContent
    Navigate Heroku Home Page
    Navigate Dynamic Content Page

    # Verify Dynamic Content Changed metodu True/False doner.
    # Bu degeri yakalayip kontrol ediyoruz.
    ${is_changed}=    Verify Dynamic Content Changed
    Should Be True    ${is_changed}    HATA: Dinamik icerik degismedi!

    Close Driver
