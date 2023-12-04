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
        self.type(CheckoutOneButtonLocators.first_name_input, firstname)
        self.type(CheckoutOneButtonLocators.last_name_input, lastname)
        self.type(CheckoutOneButtonLocators.zip_code_input, zip_code)
        self.click(CheckoutOneButtonLocators.continue_button)
