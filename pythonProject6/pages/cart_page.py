from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import allure

from utilities.logger import Logger


class Cart_page(Base):
    url ="https://www.dns-shop.ru/"
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    """Locators"""

    check_button = "//button[@id='checkout']"

    """Getters"""
    def get_check_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_button)))

    """Actions"""

    def click_check_button(self):
        self.get_check_button().click()
        print("click check button")

    """Methods"""

    def product_confirmation(self):
         with allure.step("product confirmation"):
             Logger.add_start_step(method='product_confirmation')
             self.get_current_url()
             self.click_check_button()
             Logger.add_end_step(url=self.browser.current_url, method='product_confirmation')







