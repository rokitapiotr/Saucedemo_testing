import pytest


@pytest.fixture
def valid_user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.fixture
def valid_delivery_data():
    return 'Piotr', 'Rokita', '55-555'
