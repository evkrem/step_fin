from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.ID, "id_registration-password2")

class ProductBasketLocator():
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT = (By.TAG_NAME, "h1")
    BY_PRODUCT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    COST_BY_PRODUCT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")

