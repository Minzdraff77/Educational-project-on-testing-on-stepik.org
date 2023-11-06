from pages.base_page import BasePage
from pages.locators import BasketPageLocators as BPL

class BasketPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #     super(BasketPage, self).__init__(*args, **kwargs)
    def should_be_empty_basket(self):
        '''
        проверка, что в корзине нет товаров
        '''
        assert super().is_not_element_present(*BPL.INFO_PRODUCT_IN_BASKET)
    
    def should_be_basket_message(self):
        '''
        проверка, что есть сообщение о пустой корзине
        '''
        assert super().is_element_present(*BPL.BASKET_MESSAGE_EMPTY)