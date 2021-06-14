from robot.libraries.BuiltIn import BuiltIn
from CPLocators import CPLocators
from OrderPageLocators import OrderPageLocators
from OrderData import OrderData
from CustomerData import CustomerData

bi = BuiltIn()
sl = BuiltIn().get_library_instance('SeleniumLibrary')


class CustomerPage(CPLocators, OrderPageLocators, OrderData, CustomerData):
    # ---------------Customer Sign In--------------- #
    def login_as_customer(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', CPLocators.login_form)
        bi.run_keyword('Input text', CPLocators.email_field, CustomerData.customer_email)
        bi.run_keyword('Input password', CPLocators.password_field, CustomerData.customer_password)
        bi.run_keyword('Click button', CPLocators.submit_login_button)
        bi.run_keyword('Wait until page contains element', CPLocators.customer_page)

    # 1. Check user can create an order name and choose responsible person using valid data
    def go_to_order_creation_page(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', CPLocators.order_creation)
        bi.run_keyword('Mouse over', CPLocators.order_creation)
        bi.run_keyword('Click link', CPLocators.order_creation)
        bi.run_keyword('Wait until page contains element', OrderPageLocators.create_order_btn)

    def fill_order_id(self):
        bi.run_keyword('Input text',OrderPageLocators.order_name_input, OrderData.order_id)

    def choose_responsible_person(self):
        bi.run_keyword('Click element', OrderPageLocators.resp_person_dropdown)
        bi.run_keyword('Textfield value should be', OrderPageLocators.resp_person_dropdown, OrderData.resp_person)

    def check_order_is_saved(self):
        bi.run_keyword('Wait until page contains element', OrderPageLocators.order_saved_alert)

    # 2. Check user can create an order name and choose responsible person using invalid data and empty field
    def click_order_name_field(self):
        bi.run_keyword('Click element', OrderPageLocators.order_name_input)

    def click_responsible_person_dropdown(self):
        bi.run_keyword('Click element', OrderPageLocators.resp_person_dropdown)

    def check_system_is_alerted(self):
        bi.run_keyword('Wait until page contains element', OrderPageLocators.required_alert)