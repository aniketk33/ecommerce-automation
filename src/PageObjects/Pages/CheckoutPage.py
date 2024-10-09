from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By
from src.TestBase.WebDriverSetup import BasePage
from utils.logger_util import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger()

    def verify_checkout_page(self):
        self.logger.info("Verifying checkout page")
        # self.logger.info(f"Current url: {self.driver.current_url}")
        return 'order' in self.driver.current_url

    def enter_cc_number(self, cc_number):
        self.logger.info(f"Entering credit card number: {cc_number}")
        self.send_keys((By.XPATH, Locator.credit_card_number_input), cc_number)

    def enter_cvv(self, cvv):
        self.logger.info(f"Entering cvv: {cvv}")
        self.send_keys((By.XPATH, Locator.cvv_input), cvv)

    def enter_name(self, name):
        self.logger.info(f"Entering name: {name}")
        self.send_keys((By.XPATH, Locator.card_name), name)

    def enter_country(self, country):
        self.logger.info(f"Entering country: {country}")
        # highlight country input field
        self.send_keys((By.XPATH, Locator.country_name_input), country)
        country_name = f'//button//span[text()=" {country}"]/ancestor-or-self::button'
        
        self.logger.info(f"Selecting country: {country} from the dropdown")
        # click the button for selected country
        self.click((By.XPATH, country_name))

    def place_order(self):
        self.logger.info("Placing order")
        self.click((By.XPATH, Locator.place_order_button))

    def verify_order_success(self):
        self.logger.info("Verifying order success")
        confirmation_text = WebDriverWait(self.driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.XPATH, Locator.order_confirmation_text))
        )
        return confirmation_text.is_displayed()
    
    def checkout(self, cc_number, cvv, name, country):
        assert self.verify_checkout_page()
        self.enter_cc_number(cc_number)
        self.enter_cvv(cvv)
        self.enter_name(name)
        self.enter_country(country)
        self.place_order()
        self.verify_order_success()
        assert True
