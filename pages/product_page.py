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

    def should_be_message_product_in_basket(self):
        # проверка на совпадения названия покупаемого продукта, с названием добавленного в корзину
        product = self.browser.find_element_by_tag_name("h1").text
        by_product = self.browser.find_element_by_css_selector(".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong").text
        print("product = ", product, "\n", "by_product = ", by_product)
        assert product == by_product, "by false product"

    def should_be_message_cost_product(self):
        # проверка на совпадения цены покупаемого продукта, с ценой добавленного в корзину
        cost_by_product = self.browser.find_element_by_css_selector(".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong").text
        cost_product = self.browser.find_element_by_css_selector(".col-sm-6.product_main .price_color").text
        assert cost_product == cost_by_product, "cost in bassket false"

