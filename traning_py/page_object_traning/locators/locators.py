from selenium.webdriver.common.by import By


class CommonLocators:
    CART_EMPTY_TITLE = (By.CSS_SELECTOR, '[class="ajax_cart_no_product"]')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, '[class="login"]')


class MainPageLocators:
    TITLE_MAIN_PAGE = 'My Store'
    TITLE_CONTACT_US = 'Contact us - My Store'
    TITLE_SEARCH_PAGE = 'Search - My Store'
    BUTTON_CONTACT_US = (By.CSS_SELECTOR, '[title="Contact Us"]')
    INPUT_SEARCH = (By.CSS_SELECTOR,
                    '[class="search_query form-control ac_input"]')
    FADED_SLEEVE_T_SHIRTS = (By.XPATH, '//ul[@id="homefeatured"]/li[1]')
    BUTTON_QUICK_VIEW = (By.CSS_SELECTOR,
                         '#homefeatured li:nth-child(1) .quick-view')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '[name="submit_search"]')
    FRAME_BUTTON_CLOSE = (By.CSS_SELECTOR,
                          '[class="fancybox-item fancybox-close"]')
    FRAME_IMAGE_PRODUCT = (By.CSS_SELECTOR, '[id="bigpic"]')
    FRAME_VIEW_BUTTON_ADD = (By.CSS_SELECTOR, '[name="Submit"]')

    # Window addition gds
    BUTTON_ADD_CART_ONE_ELEMENT = (By.CSS_SELECTOR,
                                   '[id=homefeatured] .product-container'
                                   ' [data-id-product="1"]')
    BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, '.button.exclusive-medium')
    WINDOW_CONTINUE_AND_CHECKOUT = (By.CSS_SELECTOR, '[id="layer_cart"]')

    SHOPPING_CART_STATUS_EMPTY = (By.CSS_SELECTOR,
                                  '[class="ajax_cart_no_product"]')
    SHOPPING_CART_COUNTER_ON_BUTTON = (By.CSS_SELECTOR,
                                       '[class="ajax_cart_quantity '
                                       'unvisible"]')
    BUTTON_PROCEED_CHECKOUT = (By.CSS_SELECTOR, '.button.button-medium')


class LoginAndAccountLocators:
    LOGIN_TITLE = 'Login - My Store'
    ACCOUNT_TITLE = 'My account - My Store'
    INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, '[id="email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '[id="passwd"]')
    BUTTON_SUBMIT_LOGIN = (By.CSS_SELECTOR, '[id="SubmitLogin"]')
    BUTTON_FORGOT_PASSWD = (By.CSS_SELECTOR,
                            '[title="Recover your forgotten password"]')
    TITLE_FORGOT_PASSWD = (By.CSS_SELECTOR, '[class="page-subheading"]')


class CartPageLocators:
    SHOPPING_CART_TITLE = 'Order - My Store'
    # LOCATORS CART ON MAIN PAGE
    SHOPPING_TITLE_PAGE = (By.CSS_SELECTOR, '[id="cart_title"]')
    SHOPPING_CART_BUTTON = (By.CSS_SELECTOR,
                            '[title="View my shopping cart"]')
    SHOPPING_NAVIGATION_TITLE = (By.CSS_SELECTOR,
                                 '[class="navigation_page"]')

    # LOCATORS ON SHOPPING CART
    TITLE_EMPTY_CART = (By.CSS_SELECTOR, '[class="alert alert-warning"]')
    SUMMARY_NOT_EMPTY_CART = (By.CSS_SELECTOR, '[id="cart_summary"]')
    BUTTON_DELETE_EMPTY_CART = (By.CSS_SELECTOR,
                                '[class="cart_quantity_delete"]')
