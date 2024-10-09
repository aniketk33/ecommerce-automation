from src.TestBase.WebDriverSetup import BasePage
from utils.logger_util import Logger
from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger()

    def verify_order_success_page(self):
        confirmation_text = WebDriverWait(self.driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.XPATH, Locator.order_confirmation_text))
        )
        return confirmation_text.is_displayed()

    def download_order_receipt(self):
        self.click((By.XPATH, Locator.download_details_button))

    def order_success(self):
        assert self.verify_order_success_page()
        self.download_order_receipt()
        assert True