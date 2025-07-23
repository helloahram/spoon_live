from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)

    def find_element_with_multiple_strategies(self, locators, timeout=10):
        """
        여러 로케이터 전략으로 요소 찾기
        :param locators: 로케이터 튜플 리스트 [(By, value), ...]
        :param timeout: 대기 시간
        :return: 찾은 요소
        """
        for by, value in locators:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except TimeoutException:
                self.logger.warning(f"Element not found with locator: {by}={value}")
        
        raise NoSuchElementException(f"Could not find element with any of the provided locators")

    def find(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            self.logger.error(f"Element not found: {by}={value}")
            raise

    def finds(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
        except TimeoutException:
            self.logger.error(f"Elements not found: {by}={value}")
            return []

    def click(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Cannot click element: {by}={value}. Error: {e}")
            raise

    def is_element_visible(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
