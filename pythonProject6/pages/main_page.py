from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import allure

from utilities.logger import Logger


class  Main_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser

    """locators"""

    product_1="//button[@id='add-to-cart-sauce-labs-backpack']"
    product_2="//button[@id='add-to-cart-sauce-labs-bike-light']"
    product_3="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart="//div[@id='shopping_cart_container']"
    menu="//button[@id='react-burger-menu-btn']"
    link_about="//a[@id='about_sidebar_link']"

    """Getters"""
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    """Actions"""

    def click_product_1(self):
        self.get_product_1().click()
        print("click product1")

    def click_product_2(self):
        self.get_product_2().click()
        print("click product2")

    def click_product_3(self):
        self.get_product_3().click()
        print("click product3")

    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def click_menu(self):
        self.get_cart().click()
        print("click menu")


    def click_link_about(self):
        self.get_cart().click()
        print("click link")


    """Methods"""

    def select_product_1(self):
       with allure.step("select_product_1"):
           Logger.add_start_step(method='select_product_1')
           self.get_current_url()
           self.click_product_1()
           self.click_cart()
           Logger.add_end_step(url=self.browser.current_url, method='select_product_1')



    def select_product_2(self):
        self.get_current_url()
        self.click_product_2()
        self.click_cart()

    def select_product_3(self):
       self.get_current_url()
       self.click_product_3()
       self.click_cart()

    def select_menu_about(self):
       with allure.step("select_menu_about"):
           self.get_current_url()
           self.click_menu()
           self.click_link_about()
           self.get_assert_url('https://saucelabs.com/')







