import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import MainPageLocators, CartButtonLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.mark.removing_items
@pytest.mark.parametrize("items_to_add, items_to_remove", [
    ([MainPageLocators.first_item_button], [CartButtonLocators.first_item_remove_button]),
    ([MainPageLocators.first_item_button, MainPageLocators.second_item_button],
     [CartButtonLocators.first_item_remove_button, CartButtonLocators.second_item_remove_button]),
    ([MainPageLocators.first_item_button, MainPageLocators.second_item_button,
      MainPageLocators.third_item_button],
     [CartButtonLocators.first_item_remove_button, CartButtonLocators.second_item_remove_button,
      CartButtonLocators.third_item_remove_button]),
])
def test_removing_item_from_cart_main_page(driver, valid_user_credentials, items_to_add, items_to_remove):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    for item in items_to_add:
        login_page.click(item)

    login_page.click(MainPageLocators.cart_icon)

    for item_remove in items_to_remove:
        login_page.click(item_remove)

    check_counter = MainPage(driver)

    assert not check_counter.is_displayed(
        MainPageLocators.shopping_cart_counter), "The cart counter should not be displayed"
