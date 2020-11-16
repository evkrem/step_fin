from .pages.product_page import ProductPage
from .pages.main_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import pytest
import time


# @pytest.mark.parametrize('page',[0, 1, 2, 3, 4, 5, 6,pytest.param(7, marks=pytest.mark.xfail(reason="он и должен был упасть")),8, 9])
# @pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{page}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    # page.should_not_be_success_message()  #проверяем, что сообщение не отображается
    page.add_to_basket()
    page.solve_quiz_and_get_code()

# @pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # page.should_not_be_success_message()

# @pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# @pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # page.should_be_object_disappeared()

# @pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# @pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# @pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser,link)
    page.open()
    page.click_on_product()

    product_page = ProductPage(browser,link)
    product_page.go_to_basket()

    basket_page = BasketPage(browser,link)
    basket_page.basket_has_text()
    # basket_page.basket_empty()

@pytest.mark.run
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)  #фикстура регистрации нового пользователя для каждого теста класса TestUserAddToBasketFromProductPage
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

        login = LoginPage(browser, link)
        login.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        # page.should_not_be_success_message()  #проверяем, что сообщение не отображается
        page.add_to_basket()