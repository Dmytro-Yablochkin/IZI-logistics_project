class LPLocators:
    email_field = 'css = input[name="email"]'
    password_field = 'css = input[name="password"]'

    submit_login_button = 'css = button[type="submit"]'

    # "Try carrier link"
    carrier_link = 'css = a[href="https://izi-logistics-carrier-master.netlify.app"]'
    # "Try customer link"
    customer_link = 'css = a[href="https://izi-logistics-carrier-master.netlify.app"]'

    login_form = 'css = #root main'

    customer_page = 'css = a[href="/"] :nth-child(1)'

    system_alert = 'Incorrect email or password. Please try again.'

    invalid_email_alert = 'Неправильный адрес эл. почты'
    invalid_password_alert = 'Invalid password. Must contain at least 1 digit, at least 1 lower case, at least 1 ' \
                             'upper case, at least 8 characters'

    # Language dropdown locators
    language_dropdown = 'css = div.MuiSelect-selectMenu'
    language_dropdown_list = 'css = ul.MuiMenu-list'

    language_list_english = 'css = li[data-value="en"]'
    language_list_latvian = 'css = li[data-value="lt"]'
    language_list_russian = 'css = li[data-value="ru"]'

    page_latvian = 'css = input[value="lt"]'
    page_russian = 'css = input[value="ru"]'
    page_english = 'css = input[value="en"]'
