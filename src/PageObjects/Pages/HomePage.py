from src.PageObjects.locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tutorialsninja.com/demo/index.php?route=common/home"

    def load_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()    
    
    # open dropdown menu
    def open_dropdown_menu(self):
        self.driver.find_element(By.XPATH, Locator.my_account_dropdown).click()
    
    # go to login page
    def go_to_login_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.login_val))).click()

    # go to register page
    def go_to_register_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.register_val))).click()