from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import allure

from utilities.logger import Logger

class  Finish_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    """Methods"""

    def finish(self):
       with allure.step("finish"):
           Logger.add_start_step(method='finish')
           self.get_current_url()
           self.get_assert_url('https://www.saucedemo.com/checkout-complete.html')
           self.get_screenshot()
           Logger.add_end_step(url=self.browser.current_url, method='finish')













