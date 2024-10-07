from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderSuccessPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_order_success_page(self):
        try:
            confirmation_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.order_confirmation_text))
            )
            assert confirmation_text.is_displayed(), "Order confirmation not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def download_order_receipt(self):
        self.driver.find_element(By.XPATH, Locator.download_details_button).click()

        