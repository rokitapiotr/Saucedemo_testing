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
def test_reset_app_state(driver, valid_user_credentials, items_to_add):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    for item_button in items_to_add:
        login_page.click(item_button)

    login_page.click(MainPageLocators.menu_button)
    login_page.click(MainPageLocators.reset_app_button)

    check_counter = MainPage(driver)

    assert not check_counter.is_displayed(
        MainPageLocators.shopping_cart_counter), "The cart counter should not be displayed"
