from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_and_input(self, text: str, locator: str, time=3):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).send_key(text)

    def find_and_click(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_and_chek_text(self, locator, text, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    def check_page(self, title, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.title_is(title))

    def switch_frame(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.frame_to_be_available_and_switch_to_it(locator))

    def check_invisibility_element(self, locator, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator))
