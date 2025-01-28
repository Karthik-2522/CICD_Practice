*** Settings ***
Resource    test.resource
Library    SeleniumLibrary
Test Setup    Test setup web
Test Teardown    Test Teardown web

*** Test Cases ***
login to amazon
    launch chrome
    amazon url launch
login to facebook
    launch firefox
    facebook url launch
merge reports
    launch chrome
API test
    post by id
    API Post 
    