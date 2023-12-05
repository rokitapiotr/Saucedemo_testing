from selenium.webdriver.remote.webdriver import WebDriver
from base_page import BasePage
from locators import *


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url_positive_login(self) -> str:
        return LoginPageLocators.url

    @property
    def footer_positive_login(self) -> str:
        return self.get_text(LoginPageLocators.footer)

    @property
    def expected_url_negative_login(self) -> str:
        return LoginPageLocators.url_logout

    @property
    def header_negative_login(self) -> str:
        return self.get_text(LoginPageLocators.login_header)


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url_twitter(self) -> str:
        return MainPageLocators.twitter_url

    @property
    def expected_url_facebook(self) -> str:
        return MainPageLocators.facebook_url

    @property
    def expected_url_linkedin(self) -> str:
        return MainPageLocators.linkedin_url

    @property
    def expected_div_text_a_to_z(self) -> str:
        return self.get_text(MainPageLocators.first_product_name_a_z)

    @property
    def expected_div_text_z_to_a(self) -> str:
        return self.get_text(MainPageLocators.first_product_name_z_a)

    @property
    def expected_div_text_low_to_high(self) -> str:
        return self.get_text(MainPageLocators.first_product_name_low_high)

    @property
    def expected_div_text_high_to_low(self) -> str:
        return self.get_text(MainPageLocators.first_product_name_high_low)

    @property
    def shopping_card_badge_counter(self):
        return self.get_text(MainPageLocators.shopping_cart_counter)

    @property
    def expected_url_about(self) -> str:
        return MainPageLocators.about_url


class CheckOutTwoPage(BasePage):
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


class CheckoutCompletePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_header(self):
        return self.get_text(CheckoutCompleteLocators.header_h2)

    def expected_image_displayed(self):
        return self.is_displayed(CheckoutCompleteLocators.positive_sign)
