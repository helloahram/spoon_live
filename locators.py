class MainPageLocators:
    """Main Page Element Locators"""
    LIVE_BUTTON = "xpath://android.widget.Button[@text='라이브']"
    RANDOM_LIVE_BUTTON = "id:random_live_button"

class LivePageLocators:
    """Live Page Element Locators"""
    TALK_BUTTON = "id:talk_button"
    LIVE_TITLE = "xpath://android.widget.TextView[@resource-id='live_title']"
    
    # 채팅 관련 로케이터
    CHAT_INPUT = "id:chat_input_field"
    SEND_CHAT_BUTTON = "id:send_chat_button"

class CommonLocators:
    """Common Elements Across Pages"""
    BACK_BUTTON = "id:back_button"
    HOME_BUTTON = "id:home_button"
    PROFILE_BUTTON = "id:profile_button"
