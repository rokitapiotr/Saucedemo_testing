import pytest
from lib.LoginPage import LoginPage, LoggedInUnsuccessfully
from conftest import driver

test_data = [
    ('standard_user', 'secret_peace'),
]


@pytest.mark.account_log_in
@pytest.mark.negative
@pytest.mark.parametrize("login, password", test_data)
def test_negative_login(driver, login, password):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(login, password)
    negative_logging = LoggedInUnsuccessfully(driver)

    assert negative_logging.header, "Header is not the same as expected"
    assert negative_logging.expected_url == negative_logging.current_url, "Actual URL is not the same as expected"