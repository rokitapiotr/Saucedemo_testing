import pytest
from LoginPage import LoginPage
from MainPage import MainPageTwitter
from conftest import driver
from locators import MainPageSocialMediaTwitterLocators, LoggedInSuccessfullyLocators


login_data = [
    ('standard_user', 'secret_sauce'),
]


@pytest.mark.social_media
@pytest.mark.parametrize("username, password", login_data)
def test_social_media_twitter_link(driver, username, password):

    main_page = LoginPage(driver)
    main_page.open()
    main_page.login(username, password)
    main_page.scroll_to_element(LoggedInSuccessfullyLocators.footer)
    main_page.click(MainPageSocialMediaTwitterLocators.twitter_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPageTwitter(driver)

    assert click_on_icon.expected_url == click_on_icon.current_url, "Actual URL is not the same as expected"
