from selenium.webdriver.remote.webdriver import WebDriver
from locators import LoginPageLocators, LoggedInSuccessfullyLocators, LoggedInUnsuccessfullyLocators
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

    def header(self) -> bool:
        return self.is_displayed(LoggedInUnsuccessfullyLocators.header)