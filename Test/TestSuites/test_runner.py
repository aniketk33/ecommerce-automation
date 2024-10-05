import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())
 
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_login_page import TestLoginPage
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(TestLoginPage),
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)