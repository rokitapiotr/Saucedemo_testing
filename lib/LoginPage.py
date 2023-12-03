from selenium.webdriver.remote.webdriver import WebDriver
from locators import *
from Pages import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(LoginPageLocators.url)

    def login(self, login, password):
        self.type(LoginPageLocators.input_login, login)
        self.type(LoginPageLocators.input_password, password)
        self.click(LoginPageLocators.login_button)

    def insert_delivery_details(self, firstname, lastname, zip_code):
        self.type(CheckoutOneButtonLocators.first_name_input, firstname)
        self.type(CheckoutOneButtonLocators.last_name_input, lastname)
        self.type(CheckoutOneButtonLocators.zip_code_input, zip_code)
        self.click(CheckoutOneButtonLocators.continue_button)


class LoggedInSuccessfully(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return LoggedInSuccessfullyLocators.url

    @property
    def footer(self) -> str:
        return self.get_text(LoggedInSuccessfullyLocators.footer)


class LoggedInUnsuccessfully(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return LoggedInUnsuccessfullyLocators.url

    @property
    def header(self) -> str:
        return self.get_text(LoggedInUnsuccessfullyLocators.login_header)


class CheckOutTwo(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_total_item_price(self):
        return self.get_text(CheckoutTwoButtonLocators.item_total)

    @property
    def expected_tax_total(self):
        return self.get_text(CheckoutTwoButtonLocators.item_tax)

    @property
    def expected_total(self):
        return self.get_text(CheckoutTwoButtonLocators.total_price)
