import pytest
from LoginPage import LoginPage
from MainPage import MainPageSelect
from conftest import driver
from locators import MainPageSelectLocators


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.fixture(params=['az', 'za', 'lohi', 'hilo'])
def option(request):
    return request.param


@pytest.mark.select_items
@pytest.mark.parametrize("user_credentials, option", [(('standard_user', 'secret_sauce'), 'az'),
                                                      (('standard_user', 'secret_sauce'), 'za'),
                                                      (('standard_user', 'secret_sauce'), 'lohi'),
                                                      (('standard_user', 'secret_sauce'), 'hilo')
                                                      ])
def test_select_items_functionality(driver, user_credentials, option):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(*user_credentials)
    login_page.select_div_by_value(MainPageSelectLocators.select_name_price, option)
    selected_option = MainPageSelect(driver)

    if option == 'az':
        assert selected_option.expected_div_text_a_to_z == 'Sauce Labs Backpack', f'First item for option {option} is not the same as expected'
    elif option == 'za':
        assert selected_option.expected_div_text_z_to_a == 'Test.allTheThings() T-Shirt (Red)', f'First item for option {option} is not the same as expected'
    elif option == 'lohi':
        assert selected_option.expected_div_text_low_to_high == 'Sauce Labs Onesie', f'First item for option {option} is not the same as expected'
    elif option == 'hilo':
        assert selected_option.expected_div_text_high_to_low == 'Sauce Labs Fleece Jacket', f'First item for option {option} is not the same as expected'
