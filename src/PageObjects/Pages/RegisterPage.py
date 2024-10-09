from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
import src.utilities as utils
from src.TestBase.WebDriverSetup import BasePage

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_register_page(self):
        self.click((By.XPATH, Locator.register_link))
    
    def verify_register_page(self):
        return self.find_element((By.XPATH, Locator.form_title)).text == utils.register_form_title

    def enter_first_name(self, first_name):
        self.send_keys((By.XPATH, Locator.first_name_textbox), first_name)
    
    def enter_last_name(self, last_name):
        self.send_keys((By.XPATH, Locator.last_name_textbox), last_name)

    def enter_email(self, email):
        self.send_keys((By.XPATH, Locator.email_textbox), email)

    def enter_phone(self, phone):
        self.send_keys((By.XPATH, Locator.phone_textbox), phone)

    def enter_password(self, password):
        self.send_keys((By.XPATH, Locator.password_textbox), password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys((By.XPATH, Locator.confirm_password_textbox), confirm_password)

    def click_above_18_checkbox(self):
        self.click((By.XPATH, Locator.above_18_checkbox))

    def click_register_button(self):
        self.click((By.XPATH, Locator.register_button))
    
    def redirect_to_login_page(self):
        self.click((By.XPATH, Locator.redirect_to_login))

    def verify_registration(self):
        message = 'Account Created Successfully'
        return self.find_element((By.XPATH, Locator.verify_registration)).text == message
