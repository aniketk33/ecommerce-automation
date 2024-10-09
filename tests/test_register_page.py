import sys
import os
sys.path.append(os.getcwd())

import pytest
from src.PageObjects.Pages.RegisterPage import RegisterPage
from src.PageObjects.Pages.LoginPage import LoginPage
import src.utilities as utils
from utils.helper_functions import take_screenshot
 
@pytest.mark.usefixtures("setup")
class TestRegisterPage:

    @pytest.mark.register
    def test_register_page(self):
        try:
            register_page = RegisterPage(self.driver)
            register_page.open_register_page()
            assert register_page.verify_register_page()
            register_page.enter_first_name(utils.first_name)
            register_page.enter_last_name(utils.last_name)
            register_page.enter_email(utils.email)
            register_page.enter_phone(utils.phone)
            register_page.enter_password(utils.password)
            register_page.enter_confirm_password(utils.password)
            register_page.click_above_18_checkbox()
            register_page.click_register_button()
            assert register_page.verify_registration()
            register_page.redirect_to_login_page()
            assert LoginPage(self.driver).verify_login_page()
        except Exception as error:
            take_screenshot(self.driver, "register_page")
            raise error