from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not presented in url login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.name()
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_CONFITM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()

