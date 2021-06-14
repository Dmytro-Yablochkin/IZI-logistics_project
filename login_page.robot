*** Settings ***
Documentation    Tests for Login page functionality

Library    SeleniumLibrary
Library    LoginPage/LoginPage.py

Test Setup    Open Browser    ${LOGIN_PAGE}    chrome
Test Teardown    Close all browsers

*** Variables ***
${LOGIN_PAGE}    *some address*

*** Test Cases ***

1. Check registered user can navigate to customer page using correct data
    input customer email
    input user password
    submit sign in
    check user is logged in as customer

2. Check user can navigate to carrier page using correct data
    go to carrier login page
    input carrier email
    input user password
    submit sign in
    check user is logged in as carrier

3. Check user can navigate to customer page using invalid password or email
    input wrong email
    input wrong password
    submit sign in
    check system alert

4. Check user can navigate to customer page using invalid password and email
    # using invalid email
    input invalid email
    input user password
    submit sign in
    check invalid email alert
    reload page
    #using invalid password
    input customer email
    input invalid password
    submit sign in
    check invalid password alert

5. Check user can change page language to Latvian using "language dropdown"
    change language to latvian
    check page is in latvian

6. Check user can change page language to Russian using "language dropdown"
    change language to russian
    check page is in russian

7. Check user can change page language to English using "Language dropdown"
    change language to russian
    change language to english
    check page is in english
