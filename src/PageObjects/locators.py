class Locator:
    # form title for login and registration page
    form_title = '//*[@class="login-title"]'
    
    # home page locators
    my_account_dropdown = '//ul[@class="list-inline"]/li[@class="dropdown"]/a'
    login_val = '//ul[@class="dropdown-menu dropdown-menu-right"]/li/a[text()="Login"]'
    register_val = '//ul[@class="dropdown-menu dropdown-menu-right"]/li/a[text()="Register"]'

    # Login Page Locators
    email_textbox_id = '//*[@id="input-email"]'
    password_textbox_id = '//*[@id="input-password"]'
    login_button_id = '//input[@value="Login"]'
    login_page_register_button_id = '//div[@class="well"]/a/text()'
    login_page_forgot_password_button_id = '//div[@class="form-group"]/a/text()'

    # Register Page Locators
    register_link = '//*[@routerlink="/auth/register"]'
    first_name_textbox = '//*[@id="firstName"]'
    last_name_textbox = '//*[@id="lastName"]'
    email_textbox = '//*[@id="userEmail"]'
    phone_textbox = '//*[@id="userMobile"]'
    password_textbox = '//*[@id="userPassword"]'
    confirm_password_textbox = '//*[@id="confirmPassword"]'
    # /html/body/app-root/app-register/div[1]/section[2]/div/div[2]/form/div[5]/div[1]/input
    above_18_checkbox = '//*[@type="checkbox"]'
    register_button = '//*[@id="login"]'
    verify_registration = '//*[@class="headcolor"]'
    redirect_to_login = '//*[@routerlink="/auth"]'