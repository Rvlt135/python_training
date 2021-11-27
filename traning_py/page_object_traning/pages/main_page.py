from selenium.common.exceptions import TimeoutException
from tms1_onl.igor_vanin.hm_25.pages.base_page import Page
from tms1_onl.igor_vanin.hm_25.locators.locators \
    import MainPageLocators as locator


class MainPage(Page):
    def check_screen_main_page(self):
        self.check_page(locator.TITLE_MAIN_PAGE)

    def open_contact_us(self):
        self.find_and_click(locator.BUTTON_CONTACT_US)
        self.check_page(locator.TITLE_CONTACT_US)

    def open_search_page(self):
        self.find_and_click(locator.BUTTON_SEARCH)
        self.check_page(locator.TITLE_SEARCH_PAGE)

    def add_product_on_main_page(self):
        self.find_and_click(locator.FADED_SLEEVE_T_SHIRTS)
        self.find_and_click(locator.BUTTON_ADD_CART_ONE_ELEMENT)

    def open_quick_view(self):
        self.find_and_click(locator.FADED_SLEEVE_T_SHIRTS)
        self.find_and_click(locator.BUTTON_QUICK_VIEW)
        self.find_and_click(locator.FRAME_BUTTON_CLOSE)

    def add_product_and_continue_shopping(self):
        self.find_and_click(locator.FADED_SLEEVE_T_SHIRTS)
        self.find_and_click(locator.BUTTON_ADD_CART_ONE_ELEMENT)
        self.find_and_click(locator.BUTTON_CONTINUE_SHOPPING)

    def add_product_and_checkout(self):
        self.add_product_on_main_page()
        self.find_and_click(locator.BUTTON_PROCEED_CHECKOUT)

    def check_empty_cart_on_main_page(self):
        try:
            self.find_element(locator.SHOPPING_CART_STATUS_EMPTY)
        except TimeoutException:
            print("Корзина не пуста")

    def check_element_cart_on_main_page(self):
        try:
            self.find_element(locator.
                              SHOPPING_CART_COUNTER_ON_BUTTON)
        except TimeoutException:
            print("Корзина не пуста")
