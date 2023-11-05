import pytest
from pages.product_page import ProductPage as PP


# @pytest.mark.parametrize('num_action', pytest.param("7", marks=pytest.mark.xfail), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@pytest.mark.parametrize('num_action', [pytest.param("7", marks=pytest.mark.xfail), 0, 1, 2, 3, 4, 5, 6, 8, 9])
def test_guest_can_add_product_to_basket(browser, num_action):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_action}'
    page = PP(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_item_to_cart()          # нажимаем на кнопку "Добавить в корзину"
