from .base_page import BasePage
from .locators import LoginPageLocators as LL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.url == self.browser.current_url, f"Login link {self.url} login is not presented" 
        # assert False, f"Login link {self.url} login is not presented"        

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LL.LOGIN_FORM), f"Login form is not presented {LL.LOGIN_FORM}"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LL.REGISTER_FORM), f"Register form is not presented{LL.REGISTER_FORM}"
        