from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # css селектор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # css селектор для формы регистрации
    
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[class*=btn-add-to-basket]")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    CART_MESSAGES_NAME = (By.CSS_SELECTOR, "div[class^=alert]:nth-of-type(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    CART_MESSAGES_PRICE = (By.CSS_SELECTOR, "div[class^=alert]:nth-of-type(3) .alertinner strong")
    MESSAGES_SUCCESS = (By.XPATH, '//*[@id="messages"]/div')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')#'a.btn.btn-default.navbar-btn.btn-cart.navbar-right.visible-xs-inline-block')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name^=reg]")
    
class BasketPageLocators():
    BASKET_MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    INFO_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")