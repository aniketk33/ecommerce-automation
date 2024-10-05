import unittest
from selenium import webdriver
import urllib3
 
class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.URL = "https://tutorialsninja.com/demo/index.php?route=account/login"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.set_page_load_timeout(360)
 
    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()