import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.DashboardPage import DashboardPage
from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
 
class TestDashboardPage(WebDriverSetup):
    def test_dashboard_page(self):
        try:
            # login
            self.login()            

            # dashboard page
            self.dashboard_page()
            sleep(3)

            print("Dashboard test completed successfully")
        
        except Exception as error:
            print(error)
            print("Dashboard test failed")
        
 
if __name__ == '__main__':
    unittest.main()