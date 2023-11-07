import math
import time
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import BasePageLocators as BPL
from pages.locators import BasketPageLocators as BskPL

class BasePage():
    def __init__(self, browser, url): #, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)     
    
    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        '''
        проверка, что элемент присутствует на странице
        '''
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def solve_quiz_and_get_code(self):
        '''
        решение капчи
        '''
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        '''
        проверка, что элемент не появляется в течение заданного времени
        '''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what))) # how, what (как и что ищем)
        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        '''
        проверка, что элемент исчезает в течение заданного времени
        '''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def go_to_login_page(self):
        '''
        переход на страницу логина
        '''
        link = self.browser.find_element(*BPL.LOGIN_LINK)
        link.click()
        
    def should_be_login_link(self):
        '''
        проверка, что есть ссылка на страницу логина
        '''
        assert self.is_element_present(*BPL.LOGIN_LINK), "Login link is not presented"
        
    def go_to_basket_page(self):
        '''
        переход на страницу корзины
        '''
        try:
            link = self.browser.find_element(*BPL.VIEW_BASKET)
            link.click()
        except ElementNotInteractableException:
            print(f"Element not interactable {BPL.VIEW_BASKET}")
            
    def should_be_authorized_user(self):
        assert self.is_element_present(*BPL.USER_ICON), "User icon is not presented, probably unauthorised user"
    
    def register_new_user(self, email, password):
        '''
        регистрация нового пользователя
        '''
        email_field = self.browser.find_element(*BPL.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*BPL.REGISTER_PASSWORD)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(*BPL.REGISTER_PASSWORD_CONFIRM)
        password_field_confirm.send_keys(password)
        button = self.browser.find_element(*BPL.REGISTER_BUTTON)
        button.click()
        time.sleep(10) # ожидание обработки нажатия
        
    def clear_basket(self):
        '''
        очистка корзины
        '''
        count_products = len(self.browser.find_elements(*BskPL.INFO_PRODUCT_IN_BASKET))
        for i in range(count_products): # Замена всех количеств в корзине на 0
            count_field = self.browser.find_element(By.CSS_SELECTOR, f'#id_form-{i}-quantity')
            count_field.clear()
            count_field.send_keys(0)
        button = self.browser.find_elements(*BPL.BUTTON_UPDATE)[0]
        button.click()
        time.sleep(5)

        
    def user_logout(self):
        '''
        выход из аккаунта
        '''
        button = self.browser.find_element(*BPL.LOGOUT_BUTTON)
        button.click()
        

