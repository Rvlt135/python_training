import pytest
from selenium import webdriver
from tms1_onl.igor_vanin.hm_25.pages import Worker


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture()
def pages(browser):
    """Фикстура для работы с методами всех экранов"""
    page = Worker(browser)
    page.open_screen()
    return page
