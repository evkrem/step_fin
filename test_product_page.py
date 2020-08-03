from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_product_to_bassket()         # выполняем метод страницы - переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.should_be_rigth_product_and_cost()
    time.sleep(1)



#
#
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