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

# XPATH 변수화 
${CHAT_BUTTON}        xpath=//android.widget.ImageView[@content-desc="chat button"]
${HEART_BUTTON}       xpath=//android.widget.ProgressBar[@resource-id="co.spoonme:id/prog_heart"]

*** Keywords ***
Open Spoonme Live
    Open Application    ${REMOTE_URL}    
    ...     platformName=${PLATFORM}    
    ...     deviceName=${DEVICE_ID}    
    ...     appPackage=${APP_PACKAGE}    
    ...     appActivity=${APP_ACTIVITY}    
    ...     automationName=UiAutomator2    
    ...     noReset=${True}

*** Test Cases ***
채팅 버튼 출력
    [Documentation]    방송 화면에서 채팅 버튼 출력 확인
    Wait Until Element Is Visible    ${CHAT_BUTTON}    10s
    Element Should Be Visible        ${CHAT_BUTTON}

하트 버튼 출력
    [Documentation]    방송 화면에서 하트(좋아요) 버튼 출력 확인
    Wait Until Element Is Visible    ${HEART_BUTTON}    10s
    Element Should Be Visible        ${HEART_BUTTON}

하트 버튼 선택
    [Documentation]    방송 화면에서 하트(좋아요) 버튼 선택 확인
    Wait Until Element Is Visible    ${HEART_BUTTON}    10s
    Click Element                    ${HEART_BUTTON}