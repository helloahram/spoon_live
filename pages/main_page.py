from base.base_page import BasePage
from resources.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class MainPage(BasePage):
    def select_first_dj_broadcast(self):
        """
        스푼이 선정한 DJ 영역의 첫 번째 방송 선택
        
        :return: 방송 선택 성공 여부
        """
        try:
            # 다중 로케이터 전략 사용
            element = self.find_element_with_multiple_strategies(MainPageLocators.DJ_FIRST_BROADCAST)
            element.click()
            return True
        except (TimeoutException, StaleElementReferenceException) as e:
            self.logger.warning(f"DJ 방송 선택 실패: {e}")
            return False
