import time
import allure
from selenium import webdriver
from pages.login_page import Login_page
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import Main_page


@allure.description("test_link_about")
def test_about_link(set_up):
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)

    login=Login_page(browser)
    login.avtorization()
    time.sleep(5)

    mp=Main_page(browser)
    mp.select_menu_about()






