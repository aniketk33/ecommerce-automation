# generate uniqe id for email
import uuid

# Paths
receipt_download_path = '/Users/aniketkumar/Desktop/Aniket/Interview Assignment/mnc/automation/receipts/'

# URLs
base_url = "https://rahulshettyacademy.com/client/"
dashboard_url = 'https://rahulshettyacademy.com/client/dashboard/dash'

# login test data
username = "aniket1@yopmail.com"
password = "Test@123"

# register page test data
first_name = 'Test'
last_name = 'User'
unique_id = uuid.uuid4().hex[:6].upper()
email = f'{first_name.lower()}.{last_name.lower()}{unique_id}@yopmail.com'
phone = '1234567890'
password = 'Test@123'
confirm_password = 'Test@123'

# checkout test data
cc_number = "1234567890123456"
cvv = "123"
name_on_card = "Aniket"
country = "India"

# dashboard page data
product_name = "ZARA COAT 3"