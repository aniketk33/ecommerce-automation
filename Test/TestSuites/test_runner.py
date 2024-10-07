import sys
# sys.path.append(sys.path[0] + "/...")
import os
sys.path.append(os.getcwd())
 
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts import test_login_page, test_register_page, test_dashboard_page, test_cart_page, test_checkout_page, test_order_success_page
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(test_register_page.TestRegisterPage),
        test_loader.loadTestsFromTestCase(test_login_page.TestLoginPage),
        test_loader.loadTestsFromTestCase(test_dashboard_page.TestDashboardPage),
        test_loader.loadTestsFromTestCase(test_cart_page.TestCartPage),
        test_loader.loadTestsFromTestCase(test_checkout_page.TestCheckoutPage),
        test_loader.loadTestsFromTestCase(test_order_success_page.TestOrderSuccessPage)
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)