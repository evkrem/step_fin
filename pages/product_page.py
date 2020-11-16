from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.product_name = self.browser.find_element(*ProductLocators.NAME_PRODUCT).text
        self.cost_product = self.browser.find_element(*ProductLocators.COST_PRODUCT).text
        self.browser.find_element(*ProductLocators.ADD_TO_BASKET).click()

    def check_add_right_product(self):
        assert self.product_name == self.browser.find_element(*ProductLocators.ADD_TO_BASKET_PRODUCT).text, "Product in basket other"
        assert self.cost_product == self.browser.find_element(*ProductLocators.COST_PRODUCT_IN_BASKET).text, "Cost product in basket other"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.ADD_TO_BASKET_PRODUCT), "Success message is presented, but should not be"

    def should_be_object_disappeared(self):
        assert self.is_disappeared(*ProductLocators.ADD_TO_BASKET_PRODUCT), "Object is presented, but should not be"

