from tms1_onl.igor_vanin.hm_25.pages.base_page import Page
from tms1_onl.igor_vanin.hm_25.locators.locators \
    import CommonLocators as common_locator
from tms1_onl.igor_vanin.hm_25.locators.locators \
    import LoginAndAccountLocators as login_locator


class LoginPage(Page):
    def open_login_page(self):
        self.find_and_click(common_locator.BUTTON_SIGN_IN)
        self.check_page(login_locator.LOGIN_TITLE)

    def open_account_page(self):
        login = 'ivanin@test.com'
        passwd = '1234qwer'
        self.open_login_page()
        self.func_login(login, passwd)

    def func_login(self, login: str, passwd: str):
        self.open_login_page()
        self.find_element(login_locator.INPUT_EMAIL_LOGIN).send_keys(login)
        self.find_element(login_locator.INPUT_PASSWORD).send_keys(passwd)
        self.find_element(login_locator.BUTTON_SUBMIT_LOGIN).click()
        self.check_page(login_locator.ACCOUNT_TITLE)

    def open_forgot_passwd_page(self):
        result = 'FORGOT YOUR PASSWORD?'
        self.open_login_page()
        self.find_and_click(login_locator.BUTTON_FORGOT_PASSWD)
        self.find_and_chek_text(login_locator.TITLE_FORGOT_PASSWD, result)
