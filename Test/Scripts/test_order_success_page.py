import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import unittest 
from src.TestBase.WebDriverSetup import WebDriverSetup

class TestOrderSuccessPage(WebDriverSetup):
    def test_order_success_page(self):
        try:
            # login user
            self.login()

            # navigate to dashboard page
            self.dashboard_page()

            # confirm order and proceed to checkout page
            self.cart_page()

            # checkout page
            self.checkout_page()

            # order success page
            self.order_success_page()


        except Exception as error:
            print(error)
            print("Checkout test failed")

if __name__ == '__main__':
    unittest.main()
