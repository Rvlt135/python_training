from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_and_click(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).click()

    def find_text(self, text, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    def chek_displayed(self, locator, time=3):
        try:
            return WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator))
        finally:
            return False

    def check_disabled(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator
                                             )).get_property('disabled')

    def check_url(self, url, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.url_changes(url))

    def find_and_switch_frame(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.frame_to_be_available_and_switch_to_it(locator))
