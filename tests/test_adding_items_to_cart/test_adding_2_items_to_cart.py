import pytest
from LoginPage import LoginPage
from MainPage import MainPageAddingButtons
from conftest import driver
from locators import MainPageAddingButtonLocators

login_data = [
    ('standard_user', 'secret_sauce'),
]


@pytest.mark.adding_items
@pytest.mark.parametrize("username, password", login_data)
def test_adding_2_item_to_cart(driver, username, password):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    login_page.click(MainPageAddingButtonLocators.first_item_button)
    login_page.click(MainPageAddingButtonLocators.second_item_button)
    check_counter = MainPageAddingButtons(driver)

    assert check_counter.shopping_card_badge_counter == "2", "The cart counter is not the same as expected"

