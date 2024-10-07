import src.PageObjects.locators as locators
from selenium.webdriver.common.by import By
import src.utilities as utils

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, locators.Locator.email_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, locators.Locator.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, locators.Locator.login_button_id).click()

    def verify_login_success_page(self, curr_url):
        """Navigate to the dashboard page and verify if the current URL is the dashboard page"""
        try:
            # check for successful login
            print(f'Current URL: {curr_url}')
            target_url = utils.dashboard_url
            return curr_url == target_url
        except Exception as error:
            assert False, f"Error occurred: {error}"