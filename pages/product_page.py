from .base_page import BasePage
from .locators import ProductBasketLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time

class ProductPage(BasePage):
    def add_product_to_bassket(self):
        link = self.browser.find_element(*ProductBasketLocator.ADD_BASKET)
        link.click()

    def should_be_rigth_product_and_cost(self):
        self.should_be_message_product_in_basket()
        self.should_be_message_cost_product()
        # self.should_not_be_success_message()
        self.should_be_success_message()

    def should_be_message_product_in_basket(self):
        # проверка на совпадения названия покупаемого продукта, с названием добавленного в корзину
        product = self.browser.find_element(*ProductBasketLocator.PRODUCT).text
        by_product = self.browser.find_element(*ProductBasketLocator.BY_PRODUCT).text
        print("product = ", product, "\n", "by_product = ", by_product)
        assert product == by_product, "by false product"

    def should_be_message_cost_product(self):
        # проверка на совпадения цены покупаемого продукта, с ценой добавленного в корзину
        cost_by_product = self.browser.find_element(*ProductBasketLocator.COST_BY_PRODUCT).text
        cost_product = self.browser.find_element(*ProductBasketLocator.COST_PRODUCT).text
        assert cost_product == cost_by_product, "cost in bassket false"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductBasketLocator.BY_PRODUCT), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductBasketLocator.PRODUCT), "Success message is not presented, but should be"



