class Locator:
    # form title for login and registration page
    form_title = '//*[@class="login-title"]'
    
    # dashboard page locators
    # /html/body/app-root/app-dashboard/app-sidebar/nav/ul/li[4]/button
    cart_button = '//button[@routerlink="/dashboard/cart"]' 
    add_to_cart_button = '//div[@class="card-body"]/button[text()=" Add To Cart"]'
    item_name = '//div[@class="card-body"]/h5'
    # items_list = '//*[@class="row"]//div[@class="card-body"]'
    items_list = '//div[@class="container"]//div[@class="row"]//div[@class="card-body"]'
    loader = '//ngx-spinner/div'

    # Login Page Locators
    email_textbox_id = '//*[@id="userEmail"]'
    password_textbox_id = '//*[@id="userPassword"]'
    login_button_id = '//*[@id="login"]'
    login_page_register_button_id = '//*[@class="text-reset"]'
    login_page_forgot_password_button_id = '//*[@class="forgot-password-link"]'

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

    # cart page locators
    continue_shop_button = '//div[@class="heading cf"]/button'
    # to check if any item present by checking its visibility
    buy_now_button = '//button[text()="Buy Now"]'
    checkout_button = '//button[text()="Checkout"]'

    # checkout page locators
    place_order_button = '//a[text()="Place Order "]'
    credit_card_number_input = '//div[@class="form__cc"]//input[contains(@class, "text-validated")]'
    cvv_input = '//div[@class="form__cc"]//div[contains(.,"CVV Code")]/input'
    country_name_input = '//input[@placeholder="Select Country"]'
    card_name = '//div[contains(., "Name on Card ")]/input'

    # order confirmation page
    order_confirmation_text = '//*[contains(.,"Thankyou")]'
    download_details_button = '//button[contains(., "Excel")]'