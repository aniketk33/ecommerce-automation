import sys
sys.path.append(sys.path[0] + "/...")
# import os
# sys.path.append(os.getcwd())
 
import unittest
from src.TestBase.WebDriverSetup import WebDriverSetup
 
class TestLoginPage(WebDriverSetup):
    def test_login_page(self):
        try:            
            self.login()
            
            print("User Logged in successfully")
            print("Login test completed successfully")
        
        except Exception as error:
            print(error)
            print("Login test failed")
        
 
if __name__ == '__main__':
    unittest.main()