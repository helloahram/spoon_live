*** Settings ***
Library    ../keywords/live_keywords.py    WITH NAME    Keyword


*** Keywords ***
Initialize App
    [Documentation]      각 Test Case 수행 시 환경 초기화를 위함
    Keyword.Start App

Close App
    [Documentation]      각 Test Case 수행 시 환경 초기화를 위함
    Keyword.Quit App

Check Chat Button
    ${visible}=    Keyword.Is Chat Button Visible
    RETURN    ${visible}

Check Heart Button
    ${visible}=    Keyword.Is Heart Button Visible
    RETURN    ${visible}

Click Heart Button
    ${result}=    Keyword.Click Heart Button
    RETURN    ${result}
