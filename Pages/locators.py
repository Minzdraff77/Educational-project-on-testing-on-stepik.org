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