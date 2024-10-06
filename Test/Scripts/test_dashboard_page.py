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