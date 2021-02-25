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

class GoogleLocators():
    INPUT_FIELD = (By.CSS_SELECTOR, ".gLFyf.gsfi")
    SEARCH_BNT = (By.CSS_SELECTOR, ".FPdoLc.tfB0Bf .gNO89b")
    RESULTS_ON_PAGE = (By.CSS_SELECTOR, ".g .tF2Cxc")
    RESULTS_LINKS = (By.CSS_SELECTOR, ".TbwUpd.NJjxre .iUh30")
