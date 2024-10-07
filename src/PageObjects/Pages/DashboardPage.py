from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_page(self):
        try:
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
        try:
            continue_shopping_button = self.driver.find_element(By.XPATH, Locator.continue_shop_button)
            return continue_shopping_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"