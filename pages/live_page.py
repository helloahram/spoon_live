from base.base_page import BasePage
from resources.locators import LivePageLocators
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class LivePage(BasePage):
    def is_chat_button_visible(self):
        """
        채팅 버튼 존재 여부 확인
        
        :return: 채팅 버튼 출력 여부
        """
        try:
            # 다중 로케이터 전략 사용
            self.find_element_with_multiple_strategies(LivePageLocators.CHAT_BUTTON)
            return True
        except NoSuchElementException:
            self.logger.warning("채팅 버튼을 찾을 수 없습니다.")
            return False

    def is_heart_button_visible(self):
        """
        하트(좋아요) 버튼 존재 여부 확인
        
        :return: 하트 버튼 출력 여부
        """
        try:
            # 다중 로케이터 전략 사용
            self.find_element_with_multiple_strategies(LivePageLocators.HEART_BUTTON)
            return True
        except NoSuchElementException:
            self.logger.warning("하트 버튼을 찾을 수 없습니다.")
            return False

    def click_heart_button(self):
        """
        하트(좋아요) 버튼 선택
        
        :return: 선택 성공 여부
        """
        try:
            # 다중 로케이터 전략 사용
            heart_button = self.find_element_with_multiple_strategies(LivePageLocators.HEART_BUTTON)
            heart_button.click()
            return True
        except (NoSuchElementException, WebDriverException) as e:
            self.logger.warning(f"하트 버튼 선택 실패: {e}")
            return False
