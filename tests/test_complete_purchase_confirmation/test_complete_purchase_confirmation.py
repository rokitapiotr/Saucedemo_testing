import pytest
from LoginPage import LoginPage, CheckoutComplete
from conftest import driver
from locators import *

VAT_RATE = 0.08


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.fixture
def delivery_data():
    return 'Piotr', 'Rokita', '55-555'


@pytest.mark.check_price
@pytest.mark.parametrize("items_to_add, item_prices_locators", [
    ([MainPageButtonLocators.first_item_button], [MainPageButtonLocators.first_item_price]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button],
     [MainPageButtonLocators.first_item_price, MainPageButtonLocators.second_item_price]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button,
      MainPageButtonLocators.third_item_button],
     [MainPageButtonLocators.first_item_price, MainPageButtonLocators.second_item_price,
      MainPageButtonLocators.third_item_price]),
])
def test_complete_purchase_confirmation(driver, user_credentials, items_to_add, delivery_data,
                                        item_prices_locators):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)

    for item_button in items_to_add:
        login_page.click(item_button)

    login_page.click(MainPageButtonLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*delivery_data)
    login_page.click(CheckoutTwoButtonLocators.finish_button)

    check_purchase_confirmation = CheckoutComplete(driver)

    assert check_purchase_confirmation.expected_header == 'Thank you for your order!', 'Headers are not the same'
    assert check_purchase_confirmation.is_displayed(CheckoutCompleteLocators.positive_sign), 'Image is not displayed'
