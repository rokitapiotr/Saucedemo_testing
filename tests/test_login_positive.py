import pytest
from lib.Login_page import LoginPage, LoggedInSuccessfully
from conftest import driver

test_data = [
    ('standard_user', 'secret_sauce'),
]


@pytest.mark.account_log_in
@pytest.mark.positive
@pytest.mark.parametrize("login, password", test_data)
def test_positive_login(driver, login, password):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(login, password)
    positive_logging = LoggedInSuccessfully(driver)

    assert positive_logging.footer == "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy", "Footer is not the same as expected"
    assert positive_logging.expected_url == positive_logging.current_url, "Actual URL is not the same as expected"
