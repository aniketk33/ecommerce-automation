from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
import src.utilities as utils
from src.TestBase.WebDriverSetup import BasePage
from utils.logger_util import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger()

    def verify_dashboard_page(self):
        return self.find_element((By.XPATH, Locator.cart_button)).is_displayed()

    def get_items(self):
        items = self.find_elements((By.XPATH, Locator.items_list))
        return items
    
    def click_add_to_cart(self):
        self.click((By.XPATH, Locator.add_to_cart_button))

    def click_cart_button(self):
        self.click((By.XPATH, Locator.cart_button))

    def dashboard(self):
        assert self.verify_dashboard_page()

        # get items on the dashboard page
        items = self.get_items()
        items_added = set()
        for item in items:
            item_obj = item.find_element(By.XPATH, Locator.item_name)
            if item_obj.text == utils.product_name and item_obj.text not in items_added:
                # get the add to cart button
                add_to_cart_button = item.find_element(By.XPATH, Locator.add_to_cart_button)
                add_to_cart_button.click()
                items_added.add(item_obj.text)
                # click on cart button
                self.logger.info("Item added to cart successfully")

        # wait for the loader to disappear
        self.logger.info("Waiting for loader to disappear")
        loader = self.find_element((By.XPATH, Locator.loader))
        WebDriverWait(self.driver, 20, poll_frequency=1).until(
            EC.invisibility_of_element(loader)
        )
        self.logger.info("Loader disappeared")        
        self.click_cart_button()
        self.logger.info("Clicked on cart button")

        assert self.driver.current_url == utils.cart_url