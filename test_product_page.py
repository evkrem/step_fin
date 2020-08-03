from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}" # перебираем все промоакции подставляя в ссылку лишь ее номер
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_product_to_bassket()         # выполняем метод страницы - переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.should_be_rigth_product_and_cost()
    time.sleep(1)

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_should_be_login_email(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_page()