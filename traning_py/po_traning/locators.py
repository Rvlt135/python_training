from selenium.webdriver.common.by import By


class Locators:
    # LOCATORS dynamic_controls
    CHECK_BOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    BUTTON_REMOVE = (By.CSS_SELECTOR, '[onclick="swapCheckbox()"]')
    MESSAGE_REMOVE_ADD = (By.CSS_SELECTOR, '[id="message"]')
    INPUT_EN_DIS = (By.CSS_SELECTOR, '[type="text"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, '[onclick="swapInput()"]')

    # LOCATORS herokuapp
    IFRAME_LINK = (By.CSS_SELECTOR, '[href="/iframe"]')
    IFRAME_INPUT = (By.CSS_SELECTOR, '[id="mce_0_ifr"]')
    IFRAME_INPUT_TEXT = (By.CSS_SELECTOR, '#tinymce>p')
