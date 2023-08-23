from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import allure

from utilities.logger import Logger


class Client_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser



    """locators"""

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    button_continue = "//input[@id='continue']"



    """Getters"""
    def get_enter_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_enter_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_enter_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_enter_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))



    """Actions"""
    def click_enter_first_name(self, first_name):
        self.get_enter_first_name().send_keys(first_name)
        print("enter first name")

    def click_enter_last_name(self, last_name):
        self.get_enter_last_name().send_keys(last_name)
        print("enter last name")


    def click_enter_postal_code(self, postal_code):
        self.get_enter_postal_code().send_keys(postal_code)
        print("enter postal code")

    def click_enter_button_continue(self):
        self.get_enter_button_continue().click()
        print("click button continue")

    """Methods"""

    def client_confirmation(self):
       Logger.add_start_step(method='client_confirmation')
       self.click_enter_first_name("aksana")
       self.click_enter_last_name("ivanova")
       self.click_enter_postal_code("94597")
       self.click_enter_button_continue()
       Logger.add_end_step(url=self.browser.current_url, method='client_confirmation')









