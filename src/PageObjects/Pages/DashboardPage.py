from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        # items to select
        # self.items = ['ZARA COAT 3', 'ADIDAS ORIGINAL']
        self.product_name = 'ZARA COAT 3'

    def verify_dashboard_page(self):
        try:
            # check for successful login
            cart_button = self.driver.find_element(By.XPATH, Locator.cart_button)
            return cart_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def get_items(self):
        items = self.driver.find_elements(By.XPATH, Locator.items_list)
        return items
    
    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, Locator.add_to_cart_button).click()

    def click_cart_button(self):
        self.driver.find_element(By.XPATH, Locator.cart_button).click()

    def verify_cart_page(self):
        # pass
        try:
            # check for successful login
            continue_shopping_button = self.driver.find_element(By.XPATH, Locator.continue_shop_button)
            return continue_shopping_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"