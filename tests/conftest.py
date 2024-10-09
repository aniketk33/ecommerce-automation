import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import src.utilities as utils
from src.PageObjects.Pages.LoginPage import LoginPage

@pytest.fixture(scope="class")
def setup(request):
    # Setup Chrome options (you can add more browsers)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(utils.base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()