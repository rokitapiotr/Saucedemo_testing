import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import *


@pytest.fixture
def user_credentials():
    return 'standard_user', 'secret_sauce'


@pytest.mark.social_media
def test_social_media_facebook_link(driver, user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*user_credentials)
    main_page.scroll_to_element(LoggedInSuccessfullyLocators.footer)
    main_page.click(MainPageSocialMediaFacebookLocators.facebook_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_facebook == click_on_icon.current_url, "Actual URL is not the same as expected"


@pytest.mark.social_media
def test_social_media_linkedin_link(driver, user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*user_credentials)
    main_page.scroll_to_element(LoggedInSuccessfullyLocators.footer)
    main_page.click(MainPageSocialMediaLinkedInLocators.linkedin_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_linkedin == click_on_icon.current_url, "Actual URL is not the same as expected"


@pytest.mark.social_media
def test_social_media_twitter_link(driver, user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*user_credentials)
    main_page.scroll_to_element(LoggedInSuccessfullyLocators.footer)
    main_page.click(MainPageSocialMediaTwitterLocators.twitter_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_twitter == click_on_icon.current_url, "Actual URL is not the same as expected"
