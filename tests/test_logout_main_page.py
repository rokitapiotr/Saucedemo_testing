import pytest
from assertions import LoginPage
from lib.user_interactions import UserInteractions
from conftest import driver
from locators import MainPageLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.mark.log_out
def test_logout_main_page(driver, valid_user_credentials):

    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.menu_button)
    login_page.click(MainPageLocators.logout_button)
    log_out = LoginPage(driver)

    assert log_out.expected_url_negative_login == log_out.current_url, "Actual URL is not the same as expected"
