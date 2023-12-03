import pytest
from LoginPage import LoginPage, CheckOutTwo
from conftest import driver
from locators import MainPageButtonLocators, CartButtonLocators

VAT_RATE = 0.08


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.fixture
def delivery_data():
    return 'Piotr', 'Rokita', '55-555'


@pytest.mark.parametrize("items_to_add, item_prices_locators", [
    ([MainPageButtonLocators.first_item_button], [MainPageButtonLocators.first_item_price]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button],
     [MainPageButtonLocators.first_item_price, MainPageButtonLocators.second_item_price]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button,
      MainPageButtonLocators.third_item_button],
     [MainPageButtonLocators.first_item_price, MainPageButtonLocators.second_item_price,
      MainPageButtonLocators.third_item_price]),
])
def test_adding_items_to_cart_and_checking_price(driver, user_credentials, items_to_add, delivery_data,
                                                 item_prices_locators):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)

    item_prices = []

    for item_button, item_price_locator in zip(items_to_add, item_prices_locators):
        login_page.click(item_button)
        raw_price = login_page.get_text(item_price_locator)
        item_price = float(raw_price.strip('$'))
        item_prices.append(item_price)

    login_page.click(MainPageButtonLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*delivery_data)
    total_sum_of_items = float(sum(item_prices))
    tax = round(total_sum_of_items * VAT_RATE, 2)
    total_sum = total_sum_of_items + tax
    check_prices = CheckOutTwo(driver)

    assert float(check_prices.expected_total_item_price[13:]) == round(total_sum_of_items, 2), "Values are not the same"
    assert float(check_prices.expected_tax_total[6:]) == round(tax, 2), "Values are not the same"
    assert float(check_prices.expected_total[8:]) == round(total_sum, 2), "Values are not the same"
