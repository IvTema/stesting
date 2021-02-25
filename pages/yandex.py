from selenium.common.exceptions import NoSuchElementException
from .locators import YandexLocators


class YandexPage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.btn = self.browser.find_element(*YandexLocators.LOGIN_BTN_MAINPAGE)
        self.btn.click()
        self.switch_to_new_window()

    def switch_to_new_window(self):
        self.new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(self.new_window)

    def enter_login(self, login):
        self.field = self.browser.find_element(*YandexLocators.LOGIN_INPUT_FIELD)
        self.field.send_keys(login)
        self.click_login_btn()

    def click_login_btn(self):
        self.btn2 = self.browser.find_element(*YandexLocators.LOGIN_BTN_LOGPAGE)
        self.btn2.click()

    def enter_password(self, password):
        self.field = self.browser.find_element(*YandexLocators.PASSWORD_INPUT_FIELD)
        self.field.send_keys(password)
        self.click_login_btn2()

    def click_login_btn2(self):
        self.btn2 = self.browser.find_element(*YandexLocators.LOGIN_BTN_LOGPAGE2)
        self.btn2.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def check_login_icon(self, login_name):
        assert self.is_element_present(*YandexLocators.LOGIN_ICON), "NO ICON. NOT LOGGED?"
        self.browser.find_element(*YandexLocators.LOGIN_ICON).click()
        self.icon_text = self.browser.find_element(*YandexLocators.LOGIN_ICON2).text
        assert self.icon_text == login_name, f"LOGIN NOT '{login_name}', IT '{self.icon_text}'"
