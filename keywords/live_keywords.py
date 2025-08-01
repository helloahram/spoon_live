import sys
import os
import logging

# 프로젝트 루트 경로 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from robot.api.deco import library, keyword
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.live_page import LivePage
from pages.main_page import MainPage

@library
class LiveKeywords:
    def __init__(self):
        self.driver = None
        self.live_page = None
        self.main_page = None
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    @keyword("Start App")
    def start_app(self):
        """Appium 드라이버 시작"""
        try:
            # Appium 2.x 버전용 capabilities 설정
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = "R3CW80550BN"
            options.app_package = "co.spoonme"
            options.app_activity = ".live.LiveActivity"
            options.no_reset = True

            # 드라이버 생성
            self.driver = webdriver.Remote(
                "http://localhost:4723", 
                options=options
            )
            
            # 페이지 객체 초기화
            self.live_page = LivePage(self.driver)
            self.main_page = MainPage(self.driver)
            
            self.logger.info("Appium 드라이버 시작 성공")
            return True
        except Exception as e:
            self.logger.error(f"Appium 드라이버 시작 실패: {e}")
            return False

    @keyword("Quit App")
    def quit_app(self):
        """Appium 드라이버 종료"""
        try:
            if self.driver:
                self.driver.quit()
            self.logger.info("Appium 드라이버 종료 성공")
            return True
        except Exception as e:
            self.logger.error(f"Appium 드라이버 종료 실패: {e}")
            return False
        
    @keyword("Is Chat Button Visible")
    def is_chat_button_visible(self):
        """채팅 버튼 가시성 확인"""
        try:
            result = self.live_page.is_chat_button_visible()
            self.logger.info(f"채팅 버튼 가시성: {result}")
            return result
        except Exception as e:
            self.logger.error(f"채팅 버튼 가시성 확인 실패: {e}")
            return False

    @keyword("Is Heart Button Visible")
    def is_heart_button_visible(self):
        """하트 버튼 가시성 확인"""
        try:
            result = self.live_page.is_heart_button_visible()
            self.logger.info(f"하트 버튼 가시성: {result}")
            return result
        except Exception as e:
            self.logger.error(f"하트 버튼 가시성 확인 실패: {e}")
            return False

    @keyword("Click Heart Button")
    def click_heart_button(self):
        """하트 버튼 클릭"""
        try:
            result = self.live_page.click_heart_button()
            self.logger.info(f"하트 버튼 클릭 결과: {result}")
            return result
        except Exception as e:
            self.logger.error(f"하트 버튼 클릭 실패: {e}")
            return False
