from appium.webdriver.common.appiumby import AppiumBy

class MainPageLocators:
    # 스푼이 선정한 DJ 영역의 첫 번째 방송 로케이터들
    DJ_FIRST_BROADCAST = [
        (AppiumBy.XPATH, "(//android.view.View[@resource-id='row_content_list'])[1]"),
        (AppiumBy.XPATH, "//android.view.View[contains(@resource-id, 'content_list')]"),
        (AppiumBy.XPATH, "//android.view.View[contains(@text, 'DJ')]")
    ]

class LivePageLocators:
    # 채팅 버튼 로케이터들
    CHAT_BUTTON = [
        (AppiumBy.XPATH, "//android.view.View[@content-desc='chat button']"),
        (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='chat button']"),
        (AppiumBy.XPATH, "//android.widget.Button[contains(@text, '채팅')]"),
        (AppiumBy.XPATH, "//android.view.View[contains(@text, '채팅')]")
    ]

    # 하트(좋아요) 버튼 로케이터들
    HEART_BUTTON = [
        (AppiumBy.XPATH, "//android.widget.ProgressBar[@resource-id='co.spoonme:id/prog_heart']"),
        (AppiumBy.ID, "co.spoonme:id/prog_heart"),
        (AppiumBy.XPATH, "//android.widget.ProgressBar[contains(@resource-id, 'heart')]")
    ]  
