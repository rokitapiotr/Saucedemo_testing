from selenium.webdriver.remote.webdriver import WebDriver
from base_page import BasePage
from locators import *


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url_positive_login(self) -> str:
        return LoggedInSuccessfullyLocators.url

    @property
    def footer_positive_login(self) -> str:
        return self.get_text(LoggedInSuccessfullyLocators.footer)

    @property
    def expected_url_negative_login(self) -> str:
        return LoggedInUnsuccessfullyLocators.url

    @property
    def header_negative_login(self) -> str:
        return self.get_text(LoggedInUnsuccessfullyLocators.login_header)


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url_twitter(self) -> str:
        return MainPageSocialMediaTwitterLocators.twitter_url

    @property
    def expected_url_facebook(self) -> str:
        return MainPageSocialMediaFacebookLocators.facebook_url

    @property
    def expected_url_linkedin(self) -> str:
        return MainPageSocialMediaLinkedInLocators.linkedin_url

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

    @property
    def shopping_card_badge_counter(self):
        return self.get_text(MainPageButtonLocators.shopping_cart_counter)


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


class CheckoutComplete(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_header(self):
        return self.get_text(CheckoutCompleteLocators.header_h2)

    def expected_image_displayed(self):
        return self.is_displayed(CheckoutCompleteLocators.positive_sign)
