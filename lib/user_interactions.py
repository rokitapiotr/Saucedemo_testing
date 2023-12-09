from selenium.webdriver.remote.webdriver import WebDriver
from locators import *
from base_page import BasePage


class UserInteractions(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(LoginPageLocators.url)

    def login(self, login, password):
        self.type(LoginPageLocators.input_login, login)
        self.type(LoginPageLocators.input_password, password)
        self.click(LoginPageLocators.login_button)

    def insert_delivery_details(self, firstname, lastname, zip_code):
        self.type(CheckoutOneLocators.first_name_input, firstname)
        self.type(CheckoutOneLocators.last_name_input, lastname)
        self.type(CheckoutOneLocators.zip_code_input, zip_code)
        self.click(CheckoutOneLocators.continue_button)
