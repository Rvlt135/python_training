from base_page import Page
from locators import Locators as lc


def test_herokuapp_dynamic_control(browser):
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    result_text_remove = "It's gone!"
    result_enable = "It's enabled!"
    page = Page(browser)
    page.open_page(url)
    page.find_and_click(lc.CHECK_BOX)
    page.find_and_click(lc.BUTTON_REMOVE)
    page.find_text(result_text_remove, lc.MESSAGE_REMOVE_ADD)
    page.chek_displayed(lc.CHECK_BOX)
    if page.check_disabled(lc.INPUT_EN_DIS):
        page.find_and_click(lc.ENABLE_BUTTON)
        page.find_text(result_enable, lc.MESSAGE_REMOVE_ADD)
        page.check_disabled(lc.INPUT_EN_DIS)
    else:
        print('Input enabled')


def test_herokuapp_frame(browser):
    url = 'http://the-internet.herokuapp.com/frames'
    chek_page_url = '/frames'
    result_text = 'Your content goes here.'
    page = Page(browser)
    page.open_page(url)
    page.find_and_click(lc.IFRAME_LINK)
    page.check_url(chek_page_url)
    page.find_and_switch_frame(lc.IFRAME_INPUT)
    page.find_text(result_text, lc.IFRAME_INPUT_TEXT)
