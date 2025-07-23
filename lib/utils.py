import logging
import os
from datetime import datetime
import time

class TestUtils:
    @staticmethod
    def take_screenshot(driver, test_name):
        """
        스크린샷 캡처 및 저장
        """
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        
        driver.save_screenshot(filename)
        return filename

    @staticmethod
    def setup_logging():
        """
        로깅 설정
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("test_log.txt"),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)

    @staticmethod
    def retry(max_attempts=3, delay=1):
        """
        테스트 재시도 데코레이터
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < max_attempts:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempts += 1
                        if attempts == max_attempts:
                            raise e
                        time.sleep(delay)
            return wrapper
        return decorator 