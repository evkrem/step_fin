from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK  = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_TO_BASKET_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, " .btn-group a.btn.btn-default")
    LINK_PRODUCT = (By.CSS_SELECTOR, ".col-sm-9 h3")

class BasketLocators():
    MESSAGE_BACKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_SUMMARY = (By.ID,"basket_formset")