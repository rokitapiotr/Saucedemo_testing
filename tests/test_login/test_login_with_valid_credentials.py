import pytest
from lib.LoginPage import LoginPage, LoggedInSuccessfully
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

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    positive_logging = LoggedInSuccessfully(driver)

    assert positive_logging.footer == "© 2023 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy", "Footer is not the same as expected"
    assert positive_logging.expected_url == positive_logging.current_url, "Actual URL is not the same as expected"
