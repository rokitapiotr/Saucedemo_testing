import pytest
from lib.LoginPage import LoginPage, LoggedInUnsuccessfully
from conftest import driver

test_data = [
    ('', ''),
    ('', 'secret_sauce'),
    ('standard_user', ''),
    ('useless_user', 'secret_sauce'),
    ('locked_out_user', 'secret_sauce'),
    ('standard_user', 'secret_sauce'),
    ('standard_user', 'secret_peace')
]



@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_locked_user(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoggedInUnsuccessfully(driver)

    assert negative_logging.header == "Epic sadface: Sorry, this user has been locked out.", "Header is not the same as expected"
    assert negative_logging.expected_url == negative_logging.current_url, "Actual URL is not the same as expected"
