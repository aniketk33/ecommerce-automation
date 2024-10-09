import time

def take_screenshot(driver, file_name='Test'):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(f'/Users/aniketkumar/Desktop/Aniket/Interview Assignment/mnc/automation/screenshots/{file_name}_{timestamp}.png')