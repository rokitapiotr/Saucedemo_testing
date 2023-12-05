import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import MainPageLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.fixture(params=['az', 'za', 'lohi', 'hilo'])
def select_functionality(request):
    return request.param


@pytest.mark.select_items
@pytest.mark.parametrize("select_functionality", ['az', 'za', 'lohi', 'hilo'])
def test_select_items_functionality(driver, select_functionality, valid_user_credentials):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)

    login_page.select_div_by_value(MainPageLocators.select_name_price, select_functionality)
    selected_option = MainPage(driver)

    if select_functionality == 'az':
        assert selected_option.expected_div_text_a_to_z == 'Sauce Labs Backpack', f'First item for option {select_functionality} is not the same as expected'
    elif select_functionality == 'za':
        assert selected_option.expected_div_text_z_to_a == 'Test.allTheThings() T-Shirt (Red)', f'First item for option {select_functionality} is not the same as expected'
    elif select_functionality == 'lohi':
        assert selected_option.expected_div_text_low_to_high == 'Sauce Labs Onesie', f'First item for option {select_functionality} is not the same as expected'
    elif select_functionality == 'hilo':
        assert selected_option.expected_div_text_high_to_low == 'Sauce Labs Fleece Jacket', f'First item for option {select_functionality} is not the same as expected'
