import pytest
from lib.LoginPage import LoginPage, LoggedInUnsuccessfully
from conftest import driver

test_data = [
    ('', ''),
]


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_empty_username_and_empty_password(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoggedInUnsuccessfully(driver)

    assert negative_logging.header == "Epic sadface: Username is required", "Header is not the same as expected"
    assert negative_logging.expected_url == negative_logging.current_url, "Actual URL is not the same as expected"