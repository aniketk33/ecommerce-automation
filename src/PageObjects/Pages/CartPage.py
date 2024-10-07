from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page(self):
        try:
            continue_shopping_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.continue_shop_button))
            )
            assert continue_shopping_button.is_displayed(), "Cart page not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def check_items_in_cart(self):
        try:
            buy_now = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.buy_now_button))
            )
            assert buy_now.is_displayed(), "No items in cart"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def checkout_button_visibility(self):
        try:
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.checkout_button))
            )
            assert checkout_button.is_displayed(), "Checkout button not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def click_checkout_button(self):
        self.driver.find_element(By.XPATH, Locator.checkout_button).click()
