class TestMainPage:
    def test_main_page(self, pages):
        pages.check_screen_main_page()

    def test_add_product_and_continue(self, pages):
        pages.add_product_and_continue_shopping()

    def test_open_contact_us(self, pages):
        pages.open_contact_us()

    def test_open_search_page(self, pages):
        pages.open_search_page()

    def test_close_quick_view_product(self, pages):
        pages.open_quick_view()


class TestAccountPage:
    def test_open_login_page(self, pages):
        pages.open_login_page()

    def test_open_account_page(self, pages):
        pages.open_account_page()

    def test_open_forgot_paswd_page(self, pages):
        pages.open_forgot_passwd_page()


class TestCart:
    def test_open_cart(self, pages):
        pages.open_shopping_cart()

    def test_open_cart_and_check_empty(self, pages):
        pages.open_shopping_cart()
        pages.check_empty_cart_on_cart_page()

    def test_empty_cart_on_main_page(self, pages):
        pages.check_empty_cart_on_main_page()

    def test_add_product_dropdown_cart(self, pages):
        pages.add_product_and_continue_shopping()
        pages.check_element_cart_on_main_page()

    def test_add_product_on_cart(self, pages):
        pages.add_product_and_checkout()
        pages.check_not_empty_cart()

    def test_delete_product(self, pages):
        pages.add_product_and_checkout()
        pages.delete_product_on_cart_page()
