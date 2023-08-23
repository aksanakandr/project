from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import allure

from utilities.logger import Logger


class  Payments_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    """locators"""

    finish_button="//button[@id='finish']"



    """Getters"""
    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    """Actions"""

    def click_finish_button(self):
        self.get_finish_button().click()
        print("click finish")

    """Methods"""

    def payment_confirmation(self):
       with allure.step("payment confirmation"):
           Logger.add_start_step(method='payment_confirmation')
           self.get_current_url()
           self.click_finish_button()
           Logger.add_end_step(url=self.browser.current_url, method='payment_confirmation')












