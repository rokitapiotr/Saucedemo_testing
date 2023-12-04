import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import MainPageButtonLocators


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.mark.removing_items
@pytest.mark.parametrize("items_to_add, items_to_remove", [
    ([MainPageButtonLocators.first_item_button], [MainPageButtonLocators.first_item_remove_button]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button],
     [MainPageButtonLocators.first_item_remove_button, MainPageButtonLocators.second_item_remove_button]),
    ([MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button,
      MainPageButtonLocators.third_item_button],
     [MainPageButtonLocators.first_item_remove_button, MainPageButtonLocators.second_item_remove_button,
      MainPageButtonLocators.third_item_remove_button]),
])
def test_removing_item_from_cart(driver, user_credentials, items_to_add, items_to_remove):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*user_credentials)

    for item in items_to_add:
        login_page.click(item)

    for item_remove in items_to_remove:
        login_page.click(item_remove)

    check_counter = MainPage(driver)

    assert not check_counter.is_displayed(
        MainPageButtonLocators.shopping_cart_counter), "The cart counter should not be displayed"
