from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_checkout_page(self):
        try:
            place_order_button = self.driver.find_element(By.XPATH, Locator.place_order_button)
            return place_order_button.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"

    def clear_cc_number_input(self):
        self.driver.find_element(By.XPATH, Locator.credit_card_number_input).clear()

    def enter_cc_number(self, cc_number):
        self.driver.find_element(By.XPATH, Locator.credit_card_number_input).send_keys(cc_number)

    def enter_cvv(self, cvv):
        self.driver.find_element(By.XPATH, Locator.cvv_input).send_keys(cvv)

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, Locator.card_name).send_keys(name)

    def enter_country(self, country):
        # highlight country input field
        self.driver.find_element(By.XPATH, Locator.country_name_input).send_keys(country)
        country_name = f'//button//span[text()=" {country}"]/ancestor-or-self::button'
        # click the button for selected country
        self.driver.find_element(By.XPATH, country_name).click()

    def place_order(self):
        self.driver.find_element(By.XPATH, Locator.place_order_button).click()

    def verify_order_success(self):
        try:
            confirmation_text = self.driver.find_element(By.XPATH, Locator.order_confirmation_text)
            return confirmation_text.is_displayed()
        except Exception as error:
            assert False, f"Error occurred: {error}"