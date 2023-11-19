*** Settings ***
Resource  resource.robot
Test setup  Create User And Input New Command

*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  pete  ville123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  vi  ville123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ää123  ville123
    Output Should Contain  Username should only contain English letters

Register With Valid Username And Too Short Password
    Input Credentials  ville  v123
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  villevalle
    Output Should Contain  Password must have atleast 1 number

*** Keywords ***

Create User And Input New Command
    Create User  pete  pete1234
    Input New Command