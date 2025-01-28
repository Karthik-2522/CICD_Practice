*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url} =    https://jsonplaceholder.typicode.com
${data}=    {"name":"karthik", "age":30, "location":"chennai"}
*** Keywords ***
Test setup web
    Set Screenshot Directory    C:\\Users\\Vimala\\Desktop\\Coding\\Robot_practice\\Result
Test Teardown web
    Close All Browsers
launch chrome 
    Open Browser     https://www.google.com    Chrome
launch firefox
    Open Browser     https://www.google.com    firefox

amazon url launch
    Go To    https://www.amazon.com
    Capture Page Screenshot
facebook url launch
    Go To    https://www.facebook.com
    Capture Page Screenshot
search for iphone
    Input Text    locator    text
API Get
    Create Session    jsonplaceholder    ${base_url}
    Log    ${base_url}
    ${response} =    GET On Session    jsonplaceholder    /posts    
    Should Be Equal As Numbers    ${response.status_code}    200
    ${response_json} =    To Json    ${response.text}
    ${length} =    Get Length    ${response_json}    
    Run Keyword If   ${length}>0    Log    Pass
API Post 
    Create Session    API    ${base_url}
    ${data} =    Create Dictionary    name=karthik    age=30
    ${response} =    POST On Session    API    /posts    data=${data}
    Should Be Equal As Numbers    ${response.status_code}    201
    ${response_json} =    To Json    ${response.text}
    ${name} =    Get From Dictionary    ${response_json}    name 
    ${age} =    Get From Dictionary    ${response_json}    age
    Log    ${response_json}, ${name},${age}
post by id
    Create Session  mysession  ${base_url}
    ${data}=  Create Dictionary  title=foo  body=bar  userId=1
    Log    ${data}
    ${response}=  POST On Session    mysession  /posts  json=${data}
    Status Should Be  201  ${response}
    Should Contain  ${response.json()}  title
    Should Contain  ${response.json()}  body
    Should Contain  ${response.json()}  userId
    
    