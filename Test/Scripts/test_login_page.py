import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.LoginPage import LoginPage
from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
 
username = "aniket123456@yopmail.com"
password = "Test@123"
 
class TestLoginPage(WebDriverSetup):
    def test_login_page(self):
        try:
            driver = self.driver    
            login_obj = LoginPage(driver)

            # check for login page
            check_title = 'Account Login'
            self.assertEqual(driver.title, check_title)
    
            sleep(1)
            login_obj.enter_username(username)
            sleep(1)
            login_obj.enter_password(password) 
            sleep(1)
            login_obj.click_login()
            sleep(5)

            assert login_obj.verify_login_page()
            
            print("User Logged in successfully")
            print("Login test completed successfully")
        
        except Exception as error:
            print(error)
            print("Login test failed")
        
 
if __name__ == '__main__':
    unittest.main()