from pages.yandex import YandexPage
from pages.google import GooglePage
import pytest


@pytest.mark.parametrize('link', ["http://yandex.ru"])
class Test_Yandex():
    def test_yandex_login(self, browser, link):
        page = YandexPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.enter_login("boy.tester")
        page.enter_password("boy.tester12345")
        page.check_login_icon("boy.tester@yandex.ru")

@pytest.mark.parametrize('link', ["http://google.com/"])
class Test_Google():
    def test_google_search(self, browser, link):
        page = GooglePage(browser, link)
        page.open()
        page.enter_request('купить кофемашину bork c804')
        page.check_results()
