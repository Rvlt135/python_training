from tms1_onl.igor_vanin.hm_25.pages.main_page import MainPage
from tms1_onl.igor_vanin.hm_25.pages.login_page import LoginPage
from tms1_onl.igor_vanin.hm_25.pages.shopping_cart_page import ShoppingCart


class Worker(MainPage, LoginPage, ShoppingCart):
    """Класс через наследование работает со всеми экранами"""
    """Метод для открытия нужного экрана"""
    def open_screen(self, url='http://automationpractice.com/index.php'):
        self.open_page(url)
