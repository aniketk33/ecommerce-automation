from time import sleep
import unittest
from selenium import webdriver
import urllib3
from src.PageObjects.Pages.LoginPage import LoginPage
from src.PageObjects.Pages.DashboardPage import DashboardPage
from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
 
username = "aniket1@yopmail.com"
password = "Test@123"

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.URL = "https://rahulshettyacademy.com/client/"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.set_page_load_timeout(360)
 
    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()

    def login(self):
        driver = self.driver
        login_obj = LoginPage(driver)

        # check for login page
        print("Testing Login Page")
        check_title = 'Log in'
        form_title = driver.find_element(By.XPATH, Locator.form_title).text
        assert check_title == form_title

        sleep(1)
        login_obj.enter_username(username)
        print("Username entered")
        sleep(1)
        login_obj.enter_password(password) 
        print("Password entered")
        sleep(1)
        print('Verify credentials')
        login_obj.click_login()
        sleep(5)

        assert login_obj.verify_login_success_page(driver.current_url), "Login failed"
    
    def dashboard_page(self):
        driver = self.driver
        dashboard_obj = DashboardPage(driver)
        items_added = set()

        # check for cart button
        assert dashboard_obj.verify_dashboard_page(), "Dashboard page not loaded successfully"
        print("Dashboard page loaded successfully")
        sleep(2)

        # select the given items
        items = dashboard_obj.get_items()

        # select items which are in the list
        for item in items:
            item_obj = item.find_element(By.XPATH, Locator.item_name)
            # print(f'Item: {item_obj.text}')
            if item_obj.text == dashboard_obj.product_name and item_obj.text not in items_added:
                # get the add to cart button
                add_to_cart_button = item.find_element(By.XPATH, Locator.add_to_cart_button)
                add_to_cart_button.click()
                items_added.add(item_obj.text)
                sleep(2)
                # click on cart button
                print("Item added to cart successfully")

        sleep(2)
        dashboard_obj.click_cart_button()
        print("Clicked on cart button")

        # verify add to cart page
        sleep(2)
        dashboard_obj.verify_cart_page()
        print("Cart page loaded successfully")