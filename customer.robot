*** Settings ***
Documentation    Tests for "Customer" and "Order" pages functionality

Library    SeleniumLibrary
Library    CustomerPage/CustomerPage.py

Test Setup    Open browser    ${LOGIN_PAGE}    chrome
Test Teardown    Close all browsers

*** Variables ***
${LOGIN_PAGE}    https://izi-logistics-customer-master.netlify.app/login

*** Test Cases ***
1. Check user can create an order name and choose responsible person using valid data
    login as customer
    go to order creation page
    fill order id
    choose responsible person
    check order is saved

2. Check user can create an order name and choose responsible person using invalid data and empty field
    login as customer
    go to order creation page
    click order name field
    click responsible person dropdown
    check system is alerted
