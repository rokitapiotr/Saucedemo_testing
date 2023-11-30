import pytest
from LoginPage import LoginPage
from MainPage import MainPageAddingButtons
from conftest import driver
from locators import MainPageAddingButtonLocators

login_data = [
    ('standard_user', 'secret_sauce'),
]


@pytest.mark.removing_items
@pytest.mark.parametrize("username, password", login_data)
def test_removing_item_from_cart_2(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    login_page.click(MainPageAddingButtonLocators.first_item_button)
    login_page.click(MainPageAddingButtonLocators.second_item_button)
    login_page.click(MainPageAddingButtonLocators.first_item_remove_button)
    login_page.click(MainPageAddingButtonLocators.second_item_remove_button)
    check_counter = MainPageAddingButtons(driver)

    assert not check_counter.is_displayed(MainPageAddingButtonLocators.shopping_cart_counter), "The cart counter should not be displayed"
