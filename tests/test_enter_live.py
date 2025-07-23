import unittest
import logging
import json
from appium import webdriver
from pages.main_page import MainPage
from pages.live_page import LivePage
from selenium.webdriver.common.by import By

class TestEnterLive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        # 설정 파일에서 capabilities 로드
        with open('config/appium_config.json', 'r') as f:
            self.capabilities = json.load(f)
        
        self.logger.info("Setting up Appium driver")
        self.driver = webdriver.Remote(
            self.capabilities.get('remote_url', 'http://localhost:4723/wd/hub'), 
            self.capabilities.get('desired_capabilities', {})
        )

    def tearDown(self):
        self.logger.info("Closing Appium driver")
        self.driver.quit()

    def test_enter_live_and_check_talk_button(self):
        try:
            main_page = MainPage(self.driver)
            main_page.open_random_live()
            
            live_page = LivePage(self.driver)
            talk_button_visible = live_page.is_talk_button_visible()
            
            self.assertTrue(talk_button_visible, "'채팅' 버튼이 보이지 않습니다.")
            self.logger.info("Test passed: Talk button is visible")
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            raise

if __name__ == "__main__":
    unittest.main()
