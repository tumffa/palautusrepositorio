*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  villevalo123
    Set Password Confirmation  villevalo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  villevalo123
    Set Password Confirmation  villevalo123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  villevalo
    Set Password Confirmation  villevalo
    Submit Credentials
    Register Should Fail With Message  Password must atleast 8 characters long and contain numbers or special letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  villevalo123
    Set Password Confirmation  villevalo000
    Submit Credentials
    Register Should Fail With Message  Passwords didn't match

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}