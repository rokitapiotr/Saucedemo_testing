import pytest
from assertions import CheckOutTwoPage
from user_interactions import UserInteractions
from conftest import driver
from locators import MainPageLocators, CartButtonLocators
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
def test_adding_items_to_cart_and_checking_price(driver, valid_user_credentials, items_to_add, valid_delivery_data,
                                                 item_prices_locators):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    item_prices = []

    for item_button, item_price_locator in zip(items_to_add, item_prices_locators):
        login_page.click(item_button)
        raw_price = login_page.get_text(item_price_locator)
        item_price = float(raw_price.strip('$'))
        item_prices.append(item_price)

    login_page.click(MainPageLocators.cart_icon)
    login_page.click(CartButtonLocators.checkout_button)
    login_page.insert_delivery_details(*valid_delivery_data)
    total_sum_of_items = float(sum(item_prices))
    tax = round(total_sum_of_items * VAT_RATE, 2)
    total_sum = total_sum_of_items + tax
    check_prices = CheckOutTwoPage(driver)

    assert float(check_prices.expected_total_item_price[13:]) == round(total_sum_of_items, 2), "Values are not the same"
    assert float(check_prices.expected_tax_total[6:]) == round(tax, 2), "Values are not the same"
    assert float(check_prices.expected_total[8:]) == round(total_sum, 2), "Values are not the same"
