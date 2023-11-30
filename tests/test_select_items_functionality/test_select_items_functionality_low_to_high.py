import pytest
from LoginPage import LoginPage
from MainPage import MainPageSelect
from conftest import driver
from locators import MainPageSelectLocators

OPTION = 'lohi'

login_data = [
    ('standard_user', 'secret_sauce'),
]


@pytest.mark.select_items
@pytest.mark.parametrize("username, password", login_data)
def test_select_items_functionality_low_to_high(driver, username, password):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    login_page.select_div_by_value(MainPageSelectLocators.select_name_price, OPTION)
    selected_option = MainPageSelect(driver)

    assert selected_option.expected_div_text_low_to_high == 'Sauce Labs Onesie', 'First item is not the same as expected '
