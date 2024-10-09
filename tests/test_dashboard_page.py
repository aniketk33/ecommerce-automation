import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import pytest
from src.PageObjects.Pages.DashboardPage import DashboardPage
from src.PageObjects.Pages.LoginPage import LoginPage
import src.utilities as utils
from utils.logger_util import Logger
from utils.helper_functions import take_screenshot


@pytest.mark.usefixtures("setup")
class TestDashboardPage:
    logger = Logger.get_logger()
    
    @pytest.mark.dashboard
    def test_dashboard_page(self):
        try:
            self.logger.info("Starting test: Dashboard Page")
            # login user
            LoginPage(self.driver).login(utils.username, utils.password)

            DashboardPage(self.driver).dashboard()
            self.logger.info("Dashboard test passed")
        
        except Exception as error:
            take_screenshot(self.driver, "dashboard_page")
            raise error