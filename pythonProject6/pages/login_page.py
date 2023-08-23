from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
import allure
from utilities.logger import Logger


class Login_page(Base):
    url ="https://www.saucedemo.com/"
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser


    """locators"""

    email_button = "//input[@id='user-name']"
    password = "//input[@id='password']"
    button_sing_in = "//input[@id='login-button']"
    main_word = "//span[@class='title']"



    """Getters"""
    def get_enter_email_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_button)))

    def get_enter_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button_sing_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sing_in)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))



    """Actions"""
    def click_enter_email_button(self, email):
        self.get_enter_email_button().send_keys(email)
        print("click email")

    def click_enter_password(self, password):
        self.get_enter_password().send_keys(password)
        print("click password")


    def click_enter_button_sing_in(self):
        self.get_enter_button_sing_in().click()
        print("click login  button")


    """Methods"""

    def avtorization(self):
        with allure.step("avtorization"):
            Logger.add_start_step(method='avtorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_enter_email_button("standard_user")
            self.click_enter_password("secret_sauce")
            self.click_enter_button_sing_in()
            self.get_assert_word(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.browser.current_url, method='avtorization')







