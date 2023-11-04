from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" # ссылка на страницу логина и регистрации
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                       # открываем страницу
    page.should_be_login_url()        # проверяем, что мы оказались на странице логина
    page.should_be_login_form()       # проверяем, наличие формы логина
    page.should_be_register_form()    # проверяем, наличие формы регистрации