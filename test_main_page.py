import pytest
import time
from pages.main_page import MainPage as MP
from pages.login_page import LoginPage as LP
from pages.basket_page import BasketPage as BP


@pytest.mark.login_guest
class TestLoginFromMainPage():
        
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/" # ссылка на главную страницу
        page = MP(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LP(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес открытой страницы
        login_page.should_be_login_page()# проверяем, что мы оказались на странице логина
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" # ссылка на страницу логина и регистрации
        page = LP(browser, link)   
        page.open()                       # открываем страницу
        page.should_be_login_url()
        

@pytest.mark.mod1
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    '''
    1. Гость открывает главную страницу 
    2. Переходит в корзину по кнопке в шапке
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    '''
    link = "http://selenium1py.pythonanywhere.com/" # ссылка на главную страницу
    page = MP(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                     # открываем страницу
    page.go_to_basket_page()        # выполняем метод страницы — переходим на страницу корзины
    basket_page = BP(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес открытой страницы
    basket_page.should_be_empty_basket()   # проверяем, что в корзине нет товаров



