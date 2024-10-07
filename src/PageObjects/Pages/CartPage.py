from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page(self):
        try:
            continue_shopping_button = self.driver.find_element(By.XPATH, Locator.continue_shop_button)
            return continue_shopping_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def check_items_in_cart(self):
        try:
            buy_now = self.driver.find_element(By.XPATH, Locator.buy_now_button)
            return buy_now.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def click_checkout_button(self):
        self.driver.find_element(By.XPATH, Locator.checkout_button).click()

    def verify_checkout_page(self):
        try:
            place_order_button = self.driver.find_element(By.XPATH, Locator.place_order_button)
            return place_order_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"