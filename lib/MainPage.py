from selenium.webdriver.remote.webdriver import WebDriver
from Pages import BasePage
from locators import MainPageSocialMediaTwitterLocators, MainPageSocialMediaFacebookLocators, MainPageSocialMediaLinkedInLocators


class MainPageTwitter(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return MainPageSocialMediaTwitterLocators.twitter_url


class MainPageFacebook(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return MainPageSocialMediaFacebookLocators.facebook_url


class MainPageLinkedIn(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return MainPageSocialMediaLinkedInLocators.linkedin_url
