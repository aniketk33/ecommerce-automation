import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import pytest
from src.PageObjects.Pages.DashboardPage import DashboardPage
from src.PageObjects.Pages.LoginPage import LoginPage
from src.PageObjects.Pages.CartPage import CartPage
import src.utilities as utils
from utils.logger_util import Logger
from utils.helper_functions import take_screenshot

@pytest.mark.usefixtures("setup")
class TestCartPage:
    logger = Logger.get_logger()
    
    @pytest.mark.cart
    def test_cart_page(self):
        try:
            self.logger.info("Starting test: Cart Page")
            # login user
            LoginPage(self.driver).login(utils.username, utils.password)

            # load items to cart
            DashboardPage(self.driver).dashboard()

            CartPage(self.driver).cart()

            self.logger.info("Cart test passed")
        
        except Exception as error:
            take_screenshot(self.driver, "cart_page")
            raise error