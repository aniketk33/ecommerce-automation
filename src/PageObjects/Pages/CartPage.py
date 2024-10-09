from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.TestBase.WebDriverSetup import BasePage
from utils.logger_util import Logger
import src.utilities as utils

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger()

    def verify_cart_page(self):
        self.logger.info("Verifying cart page")
        return self.driver.current_url == utils.cart_url

    def check_items_in_cart(self):
        self.logger.info("Checking items in cart")
        return self.find_element((By.XPATH, Locator.buy_now_button)).is_displayed()

    def checkout_button_visibility(self):
        return self.find_element((By.XPATH, Locator.checkout_button)).is_displayed()

    def click_checkout_button(self):
        self.logger.info("Clicking on checkout button")
        self.click((By.XPATH, Locator.checkout_button))

    def verify_checkout_page(self):
        self.logger.info("Verifying checkout page")
        return 'order?' in self.driver.current_url
    
    def cart(self):
        assert self.verify_cart_page()
        assert self.check_items_in_cart()
        assert self.checkout_button_visibility()
        self.click_checkout_button()
        assert self.verify_checkout_page()
        assert True