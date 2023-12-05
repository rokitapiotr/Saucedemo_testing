import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import MainPageLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.fixture(params=['az', 'za', 'lohi', 'hilo'])
def option(request):
    return request.param


@pytest.mark.select_items
@pytest.mark.parametrize("option", ['az', 'za', 'lohi', 'hilo'])
def test_select_items_functionality(driver, option, valid_user_credentials):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    login_page.select_div_by_value(MainPageLocators.select_name_price, option)
    selected_option = MainPage(driver)

    if option == 'az':
        assert selected_option.expected_div_text_a_to_z == 'Sauce Labs Backpack', f'First item for option {option} is not the same as expected'
    elif option == 'za':
        assert selected_option.expected_div_text_z_to_a == 'Test.allTheThings() T-Shirt (Red)', f'First item for option {option} is not the same as expected'
    elif option == 'lohi':
        assert selected_option.expected_div_text_low_to_high == 'Sauce Labs Onesie', f'First item for option {option} is not the same as expected'
    elif option == 'hilo':
        assert selected_option.expected_div_text_high_to_low == 'Sauce Labs Fleece Jacket', f'First item for option {option} is not the same as expected'
