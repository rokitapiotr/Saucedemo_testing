import pytest
from assertions import LoginPage
from lib.user_interactions import UserInteractions
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
def test_login_with_valid_credentials(driver, username, password):

    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    positive_logging = LoginPage(driver)

    assert positive_logging.footer_positive_login == "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy", "Footer is not the same as expected"
    assert positive_logging.expected_url_positive_login == positive_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_empty_username_and_empty_password(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Username is required", "Header is not the same as expected"
    assert negative_logging.expected_url_negative_login == negative_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_empty_username_and_valid_password(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Username is required", "Header is not the same as expected"
    assert negative_logging.expected_url_negative_login == negative_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_invalid_username_and_valid_password(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Username and password do not match any user in this service", "Header is not the same as expected"
    assert negative_logging.expected_url_negative_login == negative_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_locked_user(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Sorry, this user has been locked out.", "Header is not the same as expected"
    assert negative_logging.expected_url_negative_login == negative_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_valid_username_and_empty_password(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Password is required", "Header is not the same as expected"
    assert negative_logging.expected_url_negative_login == negative_logging.current_url, "Actual URL is not the same as expected"


@pytest.mark.log_in
@pytest.mark.parametrize("username, password", test_data)
def test_login_with_valid_username_and_invalid_password(driver, username, password):
    login_page = UserInteractions(driver)
    login_page.open()
    login_page.login(username, password)
    negative_logging = LoginPage(driver)

    assert negative_logging.header_negative_login == "Epic sadface: Username and password do not match any user in this service", "Header is not the same as expected"
    assert negative_logging.expected_url_positive_login == negative_logging.current_url, "Actual URL is not the same as expected"
