from .locators import GoogleLocators


class GooglePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def enter_request(self, request):
        self.field = self.browser.find_element(*GoogleLocators.INPUT_FIELD)
        self.field.send_keys(request)
        self.click_search_btn()

    def click_search_btn(self):
        self.btn = self.browser.find_element(*GoogleLocators.SEARCH_BNT)
        self.btn.click()

    def check_results(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.amount_of_results = len(self.browser.find_elements(*GoogleLocators.RESULTS_ON_PAGE))
        assert self.amount_of_results >= 10, "RESULTS LESS THAN 10"
        self.sites_names = self.browser.find_elements(*GoogleLocators.RESULTS_LINKS)
        self.sites = []
        for words in self.sites_names:
            all_words = words.text.split(" ")
            for i in all_words:
                self.sites.append(i)
        assert 'www.mvideo.ru' in self.sites, "www.mvideo.ru NOT IN LIST OF RESOULTS"