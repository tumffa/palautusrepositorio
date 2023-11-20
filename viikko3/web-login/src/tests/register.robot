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
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  villevalo123
    Set Password Confirmation  villevalo123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  villevalo
    Set Password Confirmation  villevalo
    Submit Register Credentials
    Register Should Fail With Message  Password must atleast 8 characters long and contain numbers or special letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  villevalo123
    Set Password Confirmation  villevalo000
    Submit Register Credentials
    Register Should Fail With Message  Passwords didn't match

Login After Successful Registration
    Set Username  Kalle
    Set Password  villevalo123
    Set Password Confirmation  villevalo123
    Submit Register Credentials
    Continue To Main Page
    Logout
    Set Username  Kalle
    Set Password  villevalo123
    Submit Login Credentials
    Login Should Succeed

Login After Unsuccessful Registration
    Set Username  Pelle
    Set Password  peloton
    Set Password Confirmation  peloton
    Submit Register Credentials
    Click Link  Login
    Set Username  Pelle
    Set Password  peloton
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

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

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Continue To Main Page
    Click Link  Continue to main page

Logout
    Click Button  Logout

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}