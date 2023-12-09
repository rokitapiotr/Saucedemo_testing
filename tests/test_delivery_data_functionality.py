import pytest
from assertions import CheckOutOnePage, CheckOutTwoPage
from user_interactions import UserInteractions
from conftest import driver
from locators import *
from fixtures.data_fixtures import valid_user_credentials
from documentation.crudential_data import test_delivery_data


@pytest.mark.delivery_data
@pytest.mark.parametrize('firstname, surname, postalcode', test_delivery_data)
def test_delivery_data_functionality_with_valid_data(driver, valid_user_credentials, firstname, surname, postalcode):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(firstname, surname, postalcode)
    login_page.click(CheckoutOneLocators.continue_button)
    delivery_data = CheckOutTwoPage(driver)

    assert delivery_data.expected_url == 'https://www.saucedemo.com/checkout-step-two.html', "Actual URL is not the same as expected"


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_firstname(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: First Name is required', 'Error is not the same as expected'


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_surname(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: Last Name is required', 'Error is not the same as expected'


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_postal_code(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: Postal Code is required', 'Error is not the same as expected'


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_firstname_and_surename(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: First Name is required', 'Error is not the same as expected'


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_surname_and_postal_code(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: Last Name is required', 'Error is not the same as expected'


@pytest.mark.delivery_data
@pytest.mark.parametrize("test_delivery_data", test_delivery_data)
def test_delivery_data_functionality_with_empty_firstname_and_postal_code(driver, valid_user_credentials, test_delivery_data):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*test_delivery_data)
    delivery_data = CheckOutOnePage(driver)

    assert delivery_data.error_message_output == 'Error: First Name is required', 'Error is not the same as expected'
