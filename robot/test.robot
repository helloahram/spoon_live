*** Settings ***
Library    AppiumLibrary
Library    Collections

*** Variables ***
${REMOTE_URL}    http://localhost:4723
${PLATFORM}      Android
${DEVICE_ID}     R3CW80550BN
${APP_PACKAGE}   co.spoonme
${APP_ACTIVITY}  .live.LiveActivity

*** Keywords ***
Open Spoonme Live
    Open Application    ${REMOTE_URL}    platformName=${PLATFORM}    deviceName=${DEVICE_ID}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}    automationName=UiAutomator2    noReset=${True}

*** Test Cases ***
채팅 버튼 출력
    [Documentation]    방송 화면에서 채팅 버튼 출력 확인
    Open Spoonme Live
    
    # 채팅 버튼 표시 확인 (다양한 로케이터 시도)
    Run Keyword And Ignore Error    Wait Until Element Is Visible    xpath=//android.view.View[@content-desc="chat button"]    10s
    Run Keyword And Ignore Error    Wait Until Element Is Visible    xpath=//android.widget.Button[contains(@text, '채팅')]    10s
    Run Keyword And Ignore Error    Wait Until Element Is Visible    xpath=//android.view.View[contains(@text, '채팅')]    10s
    
    ${chat_button_visible}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//android.view.View[@content-desc="chat button"]
    Run Keyword If    not ${chat_button_visible}    Element Should Be Visible    xpath=//android.widget.Button[contains(@text, '채팅')]
    
    Close Application

하트 버튼 출력
    [Documentation]    방송 화면에서 하트(좋아요) 버튼 출력 확인
    Open Spoonme Live
    
    # 하트 버튼 표시 확인
    Wait Until Element Is Visible    xpath=//android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]    10s
    Element Should Be Visible    xpath=//android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]
    
    Close Application

하트 버튼 선택
    [Documentation]    방송 화면에서 하트(좋아요) 버튼 선택 확인
    Open Spoonme Live
    
    # 하트 버튼 선택
    Wait Until Element Is Visible    xpath=//android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]    10s
    Click Element    xpath=//android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]
    
    Close Application
