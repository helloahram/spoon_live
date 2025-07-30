*** Settings ***
Library    AppiumLibrary
Library    Collections

Test Setup       Open Spoonme Live
Test Teardown    Close Application

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM}      Android
${DEVICE_ID}     R3CW80550BN
${APP_PACKAGE}   co.spoonme
${APP_ACTIVITY}  .live.LiveActivity

@{CHAT_BUTTON}
...    //android.widget.ImageView[@content-desc="chat button"]
...    //android.view.View[@content-desc="chat button"]

@{HEART_BUTTON}
...    //android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]
...    //android.widget.ProgressBar[contains(@resource-id, 'heart')]

*** Keywords ***
Open Spoonme Live
    Open Application    ${REMOTE_URL}    
    ...     platformName=${PLATFORM}    
    ...     deviceName=${DEVICE_ID}    
    ...     appPackage=${APP_PACKAGE}    
    ...     appActivity=${APP_ACTIVITY}    
    ...     automationName=UiAutomator2    
    ...     noReset=${True}

Wait For First Visible Element
    [Arguments]    @{locators}    ${timeout}=10s
    FOR    ${locator}    IN    @{locators}
        ${exists}=    Run Keyword And Return Status    Wait Until Element Is Visible    xpath=${locator}    ${timeout}
        IF    ${exists}
            RETURN    xpath=${locator}
        END
    END
    Fail    None of the locators were found on screen

*** Test Cases ***
Find Chat Button
    ${locator}    Wait For First Visible Element    @{CHAT_BUTTON}    3s
    Element Should Be Visible    ${locator}

Find Heart Button
    ${locator}    Wait For First Visible Element    @{HEART_BUTTON}    3s
    Element Should Be Visible    ${locator}

Click Heart Button
    ${locator}    Wait For First Visible Element    @{HEART_BUTTON}    3s
    Click Element    ${locator}