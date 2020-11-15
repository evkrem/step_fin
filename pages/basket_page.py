from .base_page import BasePage
from .locators import BasketLocators
import pytest

class BasketPage(BasePage):
    def basket_has_text(self):
        self.message_basket_empty = self.browser.find_element(*BasketLocators.MESSAGE_BACKET_EMPTY).text
        assert "Your basket is empty" in self.message_basket_empty, "basket is not empty"


    # @pytest.mark.xfail
    def basket_empty(self):
        assert self.is_element_present(*BasketLocators.PRODUCT_SUMMARY), "product in basket is not presented"
