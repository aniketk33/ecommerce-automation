import sys
sys.path.append(sys.path[0] + "/...")
 
import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.RegisterPage import RegisterPage
from src.PageObjects.locators import Locator
from selenium.webdriver.common.by import By

# generate uniqe id for email
import uuid

first_name = 'Test'
last_name = 'User'
unique_id = uuid.uuid4().hex[:6].upper()
email = f'{first_name.lower()}.{last_name.lower()}{unique_id}@yopmail.com'
phone = '1234567890'
password = 'Test@123'
confirm_password = 'Test@123'
 
class TestRegisterPage(WebDriverSetup):
    def test_login_page(self):
        try:
            driver = self.driver
            register_obj = RegisterPage(driver)

            sleep(2)
            register_obj.open_register_page()

            check_title = 'Register'
            form_title = driver.find_element(By.XPATH, Locator.form_title).text
            self.assertEqual(check_title, form_title)
    
            sleep(1)
            register_obj.enter_first_name(first_name)
            sleep(1)
            register_obj.enter_last_name(last_name)
            sleep(1)
            register_obj.enter_email(email)
            sleep(1)
            register_obj.enter_phone(phone)
            sleep(1)
            register_obj.enter_password(password)
            sleep(1)
            register_obj.enter_confirm_password(confirm_password)
            sleep(1)
            register_obj.click_above_18_checkbox()
            sleep(1)
            register_obj.click_register_button()
            sleep(3)

            # check for successful registration
            assert register_obj.verify_registration()

            register_obj.redirect_to_login_page()
            sleep(5)

            print("User Registered successfully")
            print("Register test completed successfully")
        
        except Exception as error:
            print(error)
            print("Register test failed")
        
 
if __name__ == '__main__':
    unittest.main()