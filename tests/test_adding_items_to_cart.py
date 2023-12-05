import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import MainPageLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.mark.adding_items
@pytest.mark.parametrize("items_to_add", [
    [MainPageLocators.first_item_button],
    [MainPageLocators.first_item_button, MainPageLocators.second_item_button],
    [MainPageLocators.first_item_button, MainPageLocators.second_item_button, MainPageLocators.third_item_button],
])
def test_adding_items_to_cart(driver, valid_user_credentials, items_to_add):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    for item_button in items_to_add:
        login_page.click(item_button)

    check_counter = MainPage(driver)

    expected_counter = len(items_to_add)
    assert check_counter.shopping_card_badge_counter == str(
        expected_counter), "The cart counter is not the same as expected"
