import datetime

class Base():

    def __init__(self, browser):
        self.browser = browser


    """Method get current url"""

    def get_current_url(self):
        get_url = self.browser.current_url
        print("current url " + get_url)

    """Method assert word"""

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%H.%M.%S")
        name_screenshot = 'screenshot'+ now_date + '.png'
        self.browser.save_screenshot('/Users/aksanakandratovich/PycharmProjects/pythonProject6/screen'+ name_screenshot)


    """Method assert url"""
    def get_assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url != result
        print("Good value url")

