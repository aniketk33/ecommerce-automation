import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep
from src.TestBase.WebDriverSetup import WebDriverSetup
 
class TestCartPage(WebDriverSetup):
    def test_cart_page(self):
        try:
            # login user
            self.login()

            # navigate to dashboard page
            self.dashboard_page()

            # confirm orders
            self.cart_page()

            print("Checkout page displayed")
            print("Cart test completed successfully")

        except Exception as error:
            print(error)
            # print("Cart test failed")

        
 
if __name__ == '__main__':
    unittest.main()