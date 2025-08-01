*** Settings ***
Library    ../keywords/live_keywords.py    WITH NAME    Keyword


*** Keywords ***
Initialize App
    Start App

Close App
    Quit App

Check Chat Button
    ${visible}=    Keyword.Is Chat Button Visible
    RETURN    ${visible}

Check Heart Button
    ${visible}=    Keyword.Is Heart Button Visible
    RETURN    ${visible}

Click Heart Button
    ${result}=    Keyword.Click Heart Button
    RETURN    ${result}
