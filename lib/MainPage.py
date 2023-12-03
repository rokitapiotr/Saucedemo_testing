from selenium.webdriver.remote.webdriver import WebDriver
from Pages import BasePage
from locators import *


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


class MainPageSelect(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_div_text_a_to_z(self) -> str:
        return self.get_text(MainPageSelectAtoZLocators.first_product_name)

    @property
    def expected_div_text_z_to_a(self) -> str:
        return self.get_text(MainPageSelectZtoALocators.first_product_name)

    @property
    def expected_div_text_low_to_high(self) -> str:
        return self.get_text(MainPageSelectLowToHighLocators.first_product_name)

    @property
    def expected_div_text_high_to_low(self) -> str:
        return self.get_text(MainPageSelectHighToLowLocators.first_product_name)


class MainPageAddingButtons(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def shopping_card_badge_counter(self):
        return self.get_text(MainPageButtonLocators.shopping_cart_counter)
