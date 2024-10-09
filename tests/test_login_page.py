import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import pytest
from src.PageObjects.Pages.LoginPage import LoginPage
import src.utilities as utils
from utils.logger_util import Logger
from utils.helper_functions import take_screenshot


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    logger = Logger.get_logger()
    
    # define parameters from an excel file
    # @pytest.mark.parametrize("username, password", utils.get_credentials())
    @pytest.mark.login
    def test_login_page(self):
        try:
            self.logger.info("Starting test: Valid Login")
            LoginPage(self.driver).login(utils.username, utils.password)
            self.logger.info("Login test passed")

        except Exception as error:
            take_screenshot(self.driver, "login_page")
            raise error
            

    def test_failed_login(self):
        try:
            self.logger.info("Starting test: Invalid Login")
            LoginPage(self.driver).login(utils.username, password="invalid_password")

        except Exception:
            take_screenshot(self.driver, "failed_login")
            self.logger.info("Invalid login test passed")
