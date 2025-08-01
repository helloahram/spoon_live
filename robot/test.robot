*** Settings ***
Resource    ../resources/live_access.resource

Test Setup       Initialize App
Test Teardown    Close App

*** Test Cases ***
Check Chat Button Is Visible
    ${visible}=    Check Chat Button
    Should Be True    ${visible}

Check Heart Button Is Visible
    ${visible}=    Check Heart Button
    Should Be True    ${visible}

Click Heart Button If Visible
    ${visible}=    Check Heart Button
    Run Keyword If    ${visible}    Click Heart Button
