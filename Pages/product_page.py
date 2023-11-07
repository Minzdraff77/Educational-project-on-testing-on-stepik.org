from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    '''
    Object ProductPage: класс для работы с страницей продукта
    методы:
    add_item_to_cart() комплекс проверок с проверкой верификации кода
    add_item_to_cart_not_captcha() комплекс проверок без проверки верификации кода
    click_button_add_to_cart() нажатие на кнопку "Добавить в корзину"
    enter_verification_code() обработка alert с проверкой верификации кода
    verify_item_added_to_cart() проверка имени продукта в сообщениях корзины
    verify_total_price() проверка цены в сообщениях корзины
    should_not_be_success_message() проверка отсутствия сообщения об успехе
    '''

    def add_item_to_cart(self): 
        self.click_button_add_to_cart()
        self.enter_verification_code()
        self.verify_item_added_to_cart()
        self.verify_total_price()
    
    def add_item_to_cart_not_captcha(self): 
        self.click_button_add_to_cart()
        self.verify_item_added_to_cart()
        self.verify_total_price()
        
    def click_button_add_to_cart(self):
        button = self.browser.find_element(*PPL.ADD_TO_CART_BUTTON)
        button.click()
        assert True
        
    def enter_verification_code(self): 
        '''
        Обработка alert с решением капчи
        '''
        super().solve_quiz_and_get_code()
        
    def verify_item_added_to_cart(self): 
        # выполнить поиск имени продукта в сообщениях корзины
        product_name = self.browser.find_element(*PPL.PRODUCT_NAME).text 
        card_messages = self.browser.find_element(*PPL.CART_MESSAGES_NAME).text
        assert product_name == card_messages, f"Product name {product_name} not found in {card_messages}"
    
    def verify_total_price(self):
        # Сообщение со стоимостью корзины совпадает с ценой товара.
        product_price = self.browser.find_element(*PPL.PRODUCT_PRICE).text
        card_messages = self.browser.find_element(*PPL.CART_MESSAGES_PRICE).text
        assert product_price == card_messages, f"Product price {product_price} not found in {card_messages}"
    
    def should_not_be_success_message(self):
        assert super().is_not_element_present(*PPL.MESSAGES_SUCCESS), 'Сообщение об успехе присутствует'
    
    def verify_not_success_message(self):
        assert super().is_disappeared(*PPL.MESSAGES_SUCCESS), 'Сообщение об успехе присутствует'
        
    def register_new_user(self, email, password):
        """
        Переход на страницу логина и регистрация нового пользователя
        """
        self.go_to_login_page()
        super().register_new_user(email, password)