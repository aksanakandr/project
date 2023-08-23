import time
import allure
import pytest
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_page import Client_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page
from pages.payments_page import Payments_page

#@pytest.mark.run(order=3)

@allure.description("Test but product 1")
def test_select_product_1(set_group):
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    print("start test1")
    login=Login_page(browser)
    login.avtorization()
    time.sleep(5)

    sp=Main_page(browser)
    sp.select_product_1()
    time.sleep(6)

    cp=Cart_page(browser)
    cp.product_confirmation()
    time.sleep(6)
    print("finish test1")

    #cl_p=Client_page(browser)
    #cl_p.client_confirmation()

    #pp=Payments_page(browser)
    #pp.payment_confirmation()

    #fp=Finish_page(browser)
    #fp.finish()


#@pytest.mark.run(order=1)
#def test_select_product_2():
    #s = Service(ChromeDriverManager().install())
    #browser = webdriver.Chrome(service=s)
    #print("start test2")
    #login=Login_page(browser)
    #login.avtorization()
    #time.sleep(5)

    #sp=Main_page(browser)
    #sp.select_product_2()
    #time.sleep(6)

    #cp=Cart_page(browser)
    #cp.product_confirmation()
    #time.sleep(6)
    #print("finish test2")

#@pytest.mark.run(order=2)
#def test_select_product_3():
    #s = Service(ChromeDriverManager().install())
    #browser = webdriver.Chrome(service=s)
    ##login=Login_page(browser)
    #login.avtorization()
    #time.sleep(5)

    #sp=Main_page(browser)
    #sp.select_product_3()
    #time.sleep(6)

    #cp=Cart_page(browser)
    #cp.product_confirmation()
    #time.sleep(6)
    #print("finish test3")


