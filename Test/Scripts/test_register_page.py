import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())
 
import unittest
from src.TestBase.WebDriverSetup import WebDriverSetup

 
class TestRegisterPage(WebDriverSetup):
    def test_register_page(self):
        try:            
            self.register_page()
            print("User Registered successfully")
            print("Register test completed successfully")
        
        except Exception as error:
            print(error)
            print("Register test failed")
        
 
if __name__ == '__main__':
    unittest.main()