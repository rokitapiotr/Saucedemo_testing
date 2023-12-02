import pytest
from LoginPage import LoginPage
from MainPage import MainPageAddingButtons
from conftest import driver
from locators import MainPageAddingButtonLocators


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.mark.adding_items
@pytest.mark.parametrize("items_to_add", [
    [MainPageAddingButtonLocators.first_item_button],
    [MainPageAddingButtonLocators.first_item_button, MainPageAddingButtonLocators.second_item_button],
    [MainPageAddingButtonLocators.first_item_button, MainPageAddingButtonLocators.second_item_button,
     MainPageAddingButtonLocators.third_item_button],
])
def test_adding_items_to_cart(driver, user_credentials, items_to_add):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)

    check_counter = MainPageAddingButtons(driver)

    for item_button in items_to_add:
        login_page.click(item_button)

    expected_counter = len(items_to_add)
    assert check_counter.shopping_card_badge_counter == str(
        expected_counter), "The cart counter is not the same as expected"
