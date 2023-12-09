import pytest
from assertions import LoginPage
from user_interactions import UserInteractions
from conftest import driver
from locators import *
from fixtures.data_fixtures import valid_user_credentials, valid_delivery_data

VAT_RATE = 0.08


@pytest.mark.check_price
@pytest.mark.parametrize("items_to_add, item_prices_locators", [
    ([MainPageLocators.first_item_button], [CartButtonLocators.first_item_price]),
    ([MainPageLocators.first_item_button, MainPageLocators.second_item_button],
     [CartButtonLocators.first_item_price, CartButtonLocators.second_item_price]),
    ([MainPageLocators.first_item_button, MainPageLocators.second_item_button,
      MainPageLocators.third_item_button],
     [CartButtonLocators.first_item_price, CartButtonLocators.second_item_price,
      CartButtonLocators.third_item_price]),
])
def test_complete_purchase_confirmation_back_home_button(driver, valid_user_credentials, items_to_add,
                                                         valid_delivery_data,
                                                         item_prices_locators):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    for item_button in items_to_add:
        login_page.click(item_button)

    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*valid_delivery_data)
    login_page.click(CheckoutTwoLocators.finish_button)
    login_page.click(CheckoutCompleteLocators.back_home_button)

    main_page = LoginPage(driver)

    assert main_page.expected_url_positive_login == 'https://www.saucedemo.com/inventory.html', "Actual URL is not the same as expected"
