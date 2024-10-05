import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.HomePage import HomePage
 
class TestHomePage(WebDriverSetup):
    def test_home_page(self):
        try:
            driver = self.driver    
            home_obj = HomePage(driver)

            home_obj.load_page()
            assert driver.title == 'Your Store'
            print("Home page loaded successfully")

            # open dropdown menu
            sleep(1)
            home_obj.open_dropdown_menu()
            sleep(2)

            # # go to register page
            # home_obj.go_to_register_page()
            # sleep(2)
            # # check for register page
            # check_title = 'Register Account'
            # sleep(5)
            # self.assertEqual(driver.title, check_title)
            # print("Register page loaded successfully")

            # go to login page
            home_obj.go_to_login_page()
            sleep(2)
            # check for login page
            check_title = 'Account Login'
            sleep(3)
            self.assertEqual(driver.title, check_title)
            print("Login page loaded successfully")

            print("Home Page test completed successfully")
        
        except Exception as error:
            print(error)
            print("Home Page test failed")
        
 
if __name__ == '__main__':
    unittest.main()