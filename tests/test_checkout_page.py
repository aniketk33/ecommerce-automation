import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import pytest
from src.PageObjects.Pages.DashboardPage import DashboardPage
from src.PageObjects.Pages.LoginPage import LoginPage
from src.PageObjects.Pages.CartPage import CartPage
from src.PageObjects.Pages.CheckoutPage import CheckoutPage
import src.utilities as utils
from utils.logger_util import Logger
from utils.helper_functions import take_screenshot

@pytest.mark.usefixtures("setup")
class TestCheckoutPage:
    logger = Logger.get_logger()
    
    @pytest.mark.checkout
    def test_checkout_page(self):
        try:
            self.logger.info("Starting test: Checkout Page")
            # login user
            LoginPage(self.driver).login(utils.username, utils.password)

            # load items to cart
            DashboardPage(self.driver).dashboard()

            # proceed to checkout page
            CartPage(self.driver).cart()

            # fill the necessary details on the checkout page
            CheckoutPage(self.driver).checkout(utils.cc_number, utils.cvv, utils.name_on_card, utils.country)

            self.logger.info("Checkout test passed")
        
        except Exception as error:
            take_screenshot(self.driver, "checkout_page")
            raise error