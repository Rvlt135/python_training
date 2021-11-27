from selenium.common.exceptions import TimeoutException
from tms1_onl.igor_vanin.hm_25.pages.base_page import Page
from tms1_onl.igor_vanin.hm_25.locators.locators \
    import CartPageLocators as locator


class ShoppingCart(Page):
    def open_shopping_cart(self):
        self.find_and_click(locator.SHOPPING_CART_BUTTON)
        self.check_page(locator.SHOPPING_CART_TITLE)

    def check_empty_cart_on_cart_page(self):
        try:
            self.find_element(locator.
                              TITLE_EMPTY_CART)
        except TimeoutException:
            print("Карзина не пуста")

    def check_not_empty_cart(self):
        try:
            self.find_element(locator.SUMMARY_NOT_EMPTY_CART)
        except TimeoutException:
            print("Корзина пуста")

    def delete_product_on_cart_page(self):
        self.find_and_click(locator.BUTTON_DELETE_EMPTY_CART)
        self.check_empty_cart_on_cart_page()
