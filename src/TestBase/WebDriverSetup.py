from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver=None):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def quit(self):
        self.driver.quit()



# from time import sleep
# import unittest
# from selenium import webdriver
# import urllib3
# import src.utilities as utils
# from src.PageObjects.Pages.RegisterPage import RegisterPage
# from src.PageObjects.Pages.LoginPage import LoginPage
# from src.PageObjects.Pages.DashboardPage import DashboardPage
# from src.PageObjects.Pages.CartPage import CartPage
# from src.PageObjects.Pages.CheckoutPage import CheckoutPage
# from src.PageObjects.Pages.OrderSuccessPage import OrderSuccessPage
# from src.PageObjects.locators import Locator
# from selenium.webdriver.common.by import By


# class WebDriverSetup(unittest.TestCase):
#     def setUp(self):
#         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#         # set the download path for Chrome browser
#         prefs = {'download.default_directory' : utils.receipt_download_path}
#         options = webdriver.ChromeOptions() 
#         options.add_experimental_option('prefs', prefs)

#         options.add_argument("--headless")

#         self.driver = webdriver.Chrome(options=options)
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.driver.get(utils.base_url)
#         self.driver.set_page_load_timeout(360)
 
#     def tearDown(self):
#         if (self.driver != None):
#             print("Cleanup of test environment")
#             self.driver.close()
#             self.driver.quit()

#     def register_page(self):
#         driver = self.driver
#         register_obj = RegisterPage(driver)

#         register_obj.open_register_page()

#         register_obj.verify_register_page()
#         print("Register page loaded successfully")

#         register_obj.enter_first_name(utils.first_name)
#         print('First name entered')
#         sleep(1)

#         register_obj.enter_last_name(utils.last_name)
#         print('Last name entered')
#         sleep(1)

#         register_obj.enter_email(utils.email)
#         print("Email entered")
#         sleep(1)

#         register_obj.enter_phone(utils.phone)
#         print("Phone entered")
#         sleep(1)

#         register_obj.enter_password(utils.password)
#         print("Password entered")
#         sleep(1)

#         register_obj.enter_confirm_password(utils.confirm_password)
#         print("Confirm password entered")
#         sleep(1)

#         register_obj.click_above_18_checkbox()
#         print("Checkbox clicked")
#         sleep(1)

#         register_obj.click_register_button()
#         print("Register button clicked")
#         sleep(3)

#         # check for successful registration
#         register_obj.verify_registration()

#         register_obj.redirect_to_login_page()
#         print("Redirected to login page")
#         sleep(1)

#         LoginPage(driver).verify_login_page()
#         print("Login page loaded successfully")
#         sleep(2)


#     def login(self):
#         driver = self.driver
#         login_obj = LoginPage(driver)

#         login_obj.verify_login_page()
#         print("Login page loaded successfully")
#         sleep(1)

#         login_obj.enter_username(utils.username)
#         print("Username entered")
#         sleep(1)

#         login_obj.enter_password(utils.password) 
#         print("Password entered")
#         sleep(1)

#         print('Verify credentials')
#         login_obj.click_login()
#         sleep(1)

#         DashboardPage(driver).verify_dashboard_page()
#         sleep(2)
    
#     def dashboard_page(self):
#         driver = self.driver
#         dashboard_obj = DashboardPage(driver)
#         items_added = set()

#         # check for cart button
#         dashboard_obj.verify_dashboard_page()
#         print("Dashboard page loaded successfully")
#         sleep(1)

#         # select the given items
#         items = dashboard_obj.get_items()

#         # select items which are in the list
#         for item in items:
#             item_obj = item.find_element(By.XPATH, Locator.item_name)
#             # print(f'Item: {item_obj.text}')
#             if item_obj.text == utils.product_name and item_obj.text not in items_added:
#                 # get the add to cart button
#                 add_to_cart_button = item.find_element(By.XPATH, Locator.add_to_cart_button)
#                 add_to_cart_button.click()
#                 items_added.add(item_obj.text)
#                 sleep(1)
#                 # click on cart button
#                 print("Item added to cart successfully")
#         sleep(1)

#         dashboard_obj.click_cart_button()
#         print("Clicked on cart button")
#         sleep(1)

#         # verify add to cart page
#         CartPage(driver).verify_cart_page()
#         print("Cart page loaded successfully")
#         sleep(2)

#     def cart_page(self):
#         driver = self.driver
#         # cart page
#         cart_page = CartPage(driver)

#         # verify cart page
#         cart_page.verify_cart_page()
#         print("Cart page displayed")
#         sleep(1)

#         # check items in cart
#         cart_page.check_items_in_cart()
#         print("Items in cart")
#         sleep(1)

#         # check checkout button visibility
#         cart_page.checkout_button_visibility()
#         print("Checkout button visible")
#         sleep(1)

#         # click checkout button
#         cart_page.click_checkout_button()
#         sleep(2)
#         print("Checkout button clicked")

#         # verify checkout page
#         CheckoutPage(driver).verify_checkout_page()
#         sleep(2)

#     def checkout_page(self):
#         driver = self.driver

#         checkout = CheckoutPage(driver)
        
#         # verify checkout page
#         checkout.verify_checkout_page()
#         sleep(1)

#         # clear prefilled details
#         checkout.clear_cc_number_input()
#         print("Cleared CC number input")
#         sleep(1)

#         # enter cc number
#         checkout.enter_cc_number(utils.cc_number)
#         print("Entered CC number")
#         sleep(1)


#         # enter cvv code
#         checkout.enter_cvv(utils.cvv)
#         print("Entered CVV code")
#         sleep(1)

#         # enter name
#         checkout.enter_name(utils.name_on_card)
#         print("Entered name")
#         sleep(2)

#         # enter country
#         checkout.enter_country(utils.country)
#         print("Entered country")
#         sleep(1)

#         # place order
#         checkout.place_order()
#         print("Placed order clicked")
#         sleep(1)

#         # verify order success
#         OrderSuccessPage(driver).verify_order_success_page()
#         print("Order success verified")
#         sleep(1)

#     def order_success_page(self):
#         driver = self.driver

#         # order success page
#         checkout = OrderSuccessPage(driver)

#         # verify order success page
#         checkout.verify_order_success_page()
#         sleep(1)

#         # download order receipt
#         checkout.download_order_receipt()
#         print("Order receipt downloaded")
