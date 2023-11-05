import time
from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    '''
    Открытие страницы продукта происходит в test_product_page.py.
    1. Нажимаем на кнопку "Добавить в корзину".
    2. Вводим проверочный код в алерт и отправляем в консоль проверочный код. Используем метод solve_quiz_and_get_code() из родительского класса.
    3. Проверяем что есть сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    4. Проверяем что есть сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
    '''

    def add_item_to_cart(self): 
        self.click_button()
        self.enter_verification_code()
        self.verify_item_added_to_cart()
        self.verify_total_price()
        
    def click_button(self):
        button = self.browser.find_element(*PPL.ADD_TO_CART_BUTTON)
        button.click()
        assert True
        
    def enter_verification_code(self):
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