import pytest
from pages.product_page import ProductPage as PP
import time


# # @pytest.mark.parametrize('num_action', pytest.param("7", marks=pytest.mark.xfail), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# @pytest.mark.parametrize('num_action', [pytest.param("7", marks=pytest.mark.xfail), 0, 1, 2, 3, 4, 5, 6, 8, 9])
# def test_guest_can_add_product_to_basket(browser, num_action):
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_action}'
#     page = PP(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.add_item_to_cart()          # нажимаем на кнопку "Добавить в корзину"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = PP(browser, link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                             # открываем страницу
    page.click_button_add_to_cart()         # нажимаем на кнопку "Добавить в корзину"
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе
    


def test_guest_cant_see_success_message(browser):
    '''
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    '''
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = PP(browser, link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                             # открываем страницу
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе



@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    '''
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    '''
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = PP(browser, link)                # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.click_button_add_to_cart()         # нажимаем на кнопку "Добавить в корзину"
    page.verify_not_success_message()       # проверяем, что нет сообщения об успехе

@pytest.mark.mod1
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PP(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.mod1
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PP(browser, link)
    page.open()                 # открываем страницу
    page.go_to_login_page()
