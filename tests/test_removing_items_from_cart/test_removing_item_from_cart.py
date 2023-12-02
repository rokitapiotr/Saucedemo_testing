import pytest
from LoginPage import LoginPage
from MainPage import MainPageAddingButtons
from conftest import driver
from locators import MainPageAddingButtonLocators


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.mark.removing_items
@pytest.mark.parametrize("items_to_add, items_to_remove", [
    ([MainPageAddingButtonLocators.first_item_button], [MainPageAddingButtonLocators.first_item_remove_button]),
    ([MainPageAddingButtonLocators.first_item_button, MainPageAddingButtonLocators.second_item_button],
     [MainPageAddingButtonLocators.first_item_remove_button, MainPageAddingButtonLocators.second_item_remove_button]),
    ([MainPageAddingButtonLocators.first_item_button, MainPageAddingButtonLocators.second_item_button,
      MainPageAddingButtonLocators.third_item_button],
     [MainPageAddingButtonLocators.first_item_remove_button, MainPageAddingButtonLocators.second_item_remove_button,
      MainPageAddingButtonLocators.third_item_remove_button]),
])
def test_removing_item_from_cart(driver, user_credentials, items_to_add, items_to_remove):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)

    for item in items_to_add:
        login_page.click(item)

    for item_remove in items_to_remove:
        login_page.click(item_remove)

    check_counter = MainPageAddingButtons(driver)

    assert not check_counter.is_displayed(
        MainPageAddingButtonLocators.shopping_cart_counter), "The cart counter should not be displayed"
