from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_page(self):
        try:
            cart_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Locator.cart_button))
            )
            # print(cart_button)
            assert cart_button.is_displayed(), "Dashboard page not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def get_items(self):
        items = self.driver.find_elements(By.XPATH, Locator.items_list)
        return items
    
    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, Locator.add_to_cart_button).click()

    def click_cart_button(self):
        self.driver.find_element(By.XPATH, Locator.cart_button).click()
