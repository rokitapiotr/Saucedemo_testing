import pytest
from assertions import MainPage
from lib.user_interactions import UserInteractions
from conftest import driver
from locators import MainPageLocators
from fixtures.data_fixtures import valid_user_credentials


@pytest.mark.about_button
def test_about_button(driver, valid_user_credentials):

    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(*valid_user_credentials)
    login_page.click(MainPageLocators.menu_button)
    login_page.click(MainPageLocators.about_button)
    about = MainPage(driver)

    assert about.expected_url_about == about.current_url, "Actual URL is not the same as expected"
