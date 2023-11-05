from pages.main_page import MainPage as MP
from pages.login_page import LoginPage as LP



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" # ссылка на главную страницу
    page = MP(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LP(browser, browser.current_url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес открытой страницы
    login_page.should_be_login_page()# проверяем, что мы оказались на странице логина
    
