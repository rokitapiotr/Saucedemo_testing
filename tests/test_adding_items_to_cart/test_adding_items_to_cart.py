import pytest
from LoginPage import LoginPage
from MainPage import MainPageAddingButtons
from conftest import driver
from locators import MainPageButtonLocators


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.mark.adding_items
@pytest.mark.parametrize("items_to_add", [
    [MainPageButtonLocators.first_item_button],
    [MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button],
    [MainPageButtonLocators.first_item_button, MainPageButtonLocators.second_item_button,
     MainPageButtonLocators.third_item_button],
])
def test_adding_items_to_cart(driver, user_credentials, items_to_add):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)

    for item_button in items_to_add:
        login_page.click(item_button)

    check_counter = MainPageAddingButtons(driver)

    expected_counter = len(items_to_add)
    assert check_counter.shopping_card_badge_counter == str(
        expected_counter), "The cart counter is not the same as expected"
