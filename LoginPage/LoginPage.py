from robot.libraries.BuiltIn import BuiltIn
from LPLocators import LPLocators
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class LoginPage:
    # 1. Check registered user can navigate to customer page using correct data
    def input_customer_email(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.login_form)
        bi.run_keyword('Input text', LPLocators.email_field, UserData.customer_user_email)

    def input_user_password(self):
        bi.run_keyword('Input text', LPLocators.password_field, UserData.user_password)

    def submit_sign_in(self):
        bi.run_keyword('Click element', LPLocators.submit_login_button)

    def check_user_is_logged_in_as_customer(self):
        bi.run_keyword('Wait until page contains element', LPLocators.customer_page)

    # 2. Check user can navigate to carrier page using correct data
    def go_to_carrier_login_page(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.login_form)
        bi.run_keyword('Click link', LPLocators.carrier_link)

    def input_carrier_email(self):
        bi.run_keyword('Wait until element is visible', LPLocators.login_form)
        bi.run_keyword('Input text', LPLocators.email_field, UserData.carrier_user_email)

    def check_user_is_logged_in_as_carrier(self):
        bi.run_keyword('Wait until page contains element', LPLocators.customer_page)

    # 3. Check user can navigate to customer page using invalid password or email
    def input_wrong_email(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.login_form)
        bi.run_keyword('Input text', LPLocators.email_field, UserData.wrong_email)

    def input_wrong_password(self):
        bi.run_keyword('Input text', LPLocators.password_field, UserData.wrong_password)

    def check_system_alert(self):
        bi.run_keyword('Wait until page contains', LPLocators.system_alert)

    # 4. Check user can navigate to customer page using invalid password or email
    def input_invalid_email(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.login_form)
        bi.run_keyword('Input text', LPLocators.email_field, UserData.invalid_email)

    def input_invalid_password(self):
        bi.run_keyword('Input text', LPLocators.password_field, UserData.invalid_password)

    def check_invalid_email_alert(self):
        bi.run_keyword('Wait until page contains', LPLocators.invalid_email_alert)

    def check_invalid_password_alert(self):
        bi.run_keyword('Wait until page contains', LPLocators.invalid_password_alert)

    # 5. Check user can change page language to latvian using "language dropdown"
    def change_language_to_latvian(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_list_latvian)

    def check_page_is_in_latvian(self):
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Element attribute value should be', LPLocators.page_latvian, 'value', 'lt')

    # 6. Check user can change page language to russian using "language dropdown"
    def change_language_to_russian(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_list_russian)

    def check_page_is_in_russian(self):
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Element attribute value should be', LPLocators.page_russian, 'value', 'ru')

    # 7. Check user can change page language to English using "language dropdown"
    def change_language_to_english(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_dropdown)
        bi.run_keyword('Click element', LPLocators.language_list_english)

    def check_page_is_in_english(self):
        bi.run_keyword('Wait until element is visible', LPLocators.language_dropdown)
        bi.run_keyword('Element attribute value should be', LPLocators.page_english, 'value', 'en')