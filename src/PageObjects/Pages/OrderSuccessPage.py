from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By

class OrderSuccessPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_order_success_page(self):
        try:
            confirmation_text = self.driver.find_element(By.XPATH, Locator.order_confirmation_text)
            return confirmation_text.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def download_order_receipt(self):
        self.driver.find_element(By.XPATH, Locator.download_details_button).click()

        