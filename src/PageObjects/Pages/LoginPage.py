from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
import src.utilities as utils
from utils.logger_util import Logger
from src.TestBase.WebDriverSetup import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger()
    
    def verify_login_page(self):
        self.logger.info("Verifying login page")
        return self.find_element((By.XPATH, Locator.form_title)).text == utils.login_form_title

    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        self.send_keys((By.XPATH, Locator.email_textbox_id), username)

    def enter_password(self, password):
        self.send_keys((By.XPATH, Locator.password_textbox_id), password)

    def click_login(self):
        self.click((By.XPATH, Locator.login_button_id))

    def login(self, username, password):
        assert self.verify_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(utils.dashboard_url)
        )
        assert True

    