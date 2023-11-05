from pages.product_page import ProductPage as PP


# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # ссылка на тестируемую страницу
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_add_product_to_basket(browser):
    '''
    Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
    Нажимаем на кнопку "Добавить в корзину".
    *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.
    '''
    page = PP(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_item_to_cart()          # нажимаем на кнопку "Добавить в корзину"
