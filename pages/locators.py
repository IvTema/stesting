from selenium.webdriver.common.by import By


class YandexLocators():
    LOGIN_BTN_MAINPAGE = (By.CSS_SELECTOR,
                          ".button.desk-notif-card__login-enter-expanded")
    LOGIN_INPUT_FIELD = (By.CSS_SELECTOR, "#passp-field-login")
    LOGIN_BTN_LOGPAGE = (By.CSS_SELECTOR, "button.Button2")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#passp-field-passwd")
    LOGIN_BTN_LOGPAGE2 = (By.CSS_SELECTOR, ".passp-button .Button2")
    LOGIN_ICON = (By.CSS_SELECTOR, ".user-account_left-name")
    LOGIN_ICON2 = (By.CSS_SELECTOR, ".user-account__subname")