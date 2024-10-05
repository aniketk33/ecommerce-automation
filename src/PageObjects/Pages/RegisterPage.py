from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_register_page(self):
        self.driver.find_element(By.XPATH, Locator.register_link).click()

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
            message_element = self.driver.find_element(By.XPATH, Locator.verify_registration)
            return message_element.text == message
        except Exception as error:
            assert False, f"Error occurred: {error}"