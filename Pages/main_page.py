from .base_page import BasePage
from .locators import MainPageLocators as ML


class MainPage(BasePage):
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(*ML.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert  self.is_element_present(*ML.LOGIN_LINK), f"Login link is not presented{ML.LOGIN_LINK}"
        # assert False, f"Login link is not presented{ML.LOGIN_LINK}"