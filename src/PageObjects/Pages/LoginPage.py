from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import src.utilities as utils

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def verify_login_page(self):
        try:
            check_title = 'Log in'
            correct_form_title = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, Locator.form_title), check_title)
            )
            assert correct_form_title, "Login page not displayed"
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, Locator.email_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, Locator.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, Locator.login_button_id).click()