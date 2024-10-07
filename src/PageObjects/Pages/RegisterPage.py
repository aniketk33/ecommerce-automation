from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import src.utilities as utils

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_register_page(self):
        self.driver.find_element(By.XPATH, Locator.register_link).click()
    
    def verify_register_page(self):
        try:
            correct_form_title = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, Locator.form_title), utils.register_form_title)
            )
            assert correct_form_title, "Register page not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, Locator.first_name_textbox).send_keys(first_name)
    
    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, Locator.last_name_textbox).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, Locator.email_textbox).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(By.XPATH, Locator.phone_textbox).send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, Locator.password_textbox).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, Locator.confirm_password_textbox).send_keys(confirm_password)

    def click_above_18_checkbox(self):
        self.driver.find_element(By.XPATH, Locator.above_18_checkbox).click()

    def click_register_button(self):
        self.driver.find_element(By.XPATH, Locator.register_button).click()
    
    def redirect_to_login_page(self):
        self.driver.find_element(By.XPATH, Locator.redirect_to_login).click()

    def verify_registration(self):
        try:
            message = 'Account Created Successfully'
            valid_message = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, Locator.verify_registration), message)
            )
            assert valid_message, "Registration not successful"
        except Exception as error:
            assert False, f"Error occurred: {error}"