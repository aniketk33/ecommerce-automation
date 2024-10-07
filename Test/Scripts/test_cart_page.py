import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.CartPage import CartPage
 
class TestCartPage(WebDriverSetup):
    def test_cart_page(self):
        try:
            # login user
            self.login()

            # navigate to dashboard page
            self.dashboard_page()

            driver = self.driver

            # cart page
            cart_page = CartPage(driver)
            sleep(2)

            # verify cart page
            assert cart_page.verify_cart_page(), "Cart page not displayed"
            sleep(2)
            print("Cart page displayed")

            # check items in cart
            assert cart_page.check_items_in_cart(), "No items in cart"
            sleep(2)
            print("Items in cart")

            # click checkout button
            cart_page.click_checkout_button(), "Checkout button not clicked"
            sleep(2)
            print("Checkout button clicked")

            # verify checkout page
            assert cart_page.verify_checkout_page(), "Checkout page not displayed"
            sleep(2)
            print("Checkout page displayed")

            print("Cart test completed successfully")

        except Exception as error:
            print(error)
            print("Cart test failed")
        
 
if __name__ == '__main__':
    unittest.main()