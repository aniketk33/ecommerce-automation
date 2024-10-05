import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.LoginPage import LoginPage
 
username = "aniket1@yopmail.com"
password = "Test@123"
 
class TestLoginPage(WebDriverSetup):
    def test_login_page(self):
        try:
            driver = self.driver
            self.URL = "https://rahulshettyacademy.com/client/"
            self.driver.get(self.URL)
            self.driver.set_page_load_timeout(360)

            # check whether the title is correct
            self.assertIn("Let's Shop", driver.title)
    
            login_obj = LoginPage(driver)
    
            sleep(2)
            login_obj.enter_username(username)
            sleep(2)
            login_obj.enter_password(password) 
            sleep(2)
            login_obj.click_login()
            sleep(5)

            # check for successful login
            curr_url = self.driver.current_url
            print(f'Current URL: {curr_url}')
            target_url = 'https://rahulshettyacademy.com/client/dashboard/dash'        

            self.assertEqual(curr_url, target_url)
            print("User Logged in successfully")
            print("Login test completed successfully")
        
        except Exception as error:
            print(error)
            print("Login test failed")
        
 
if __name__ == '__main__':
    unittest.main()