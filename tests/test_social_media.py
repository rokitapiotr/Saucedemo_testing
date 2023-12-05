import pytest
from user_interactions import UserInteractions
from assertions import MainPage
from conftest import driver
from locators import *
from fixtures.data_fixtures import valid_user_credentials


@pytest.mark.social_media
def test_social_media_facebook_link(driver, valid_user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*valid_user_credentials)
    main_page.scroll_to_element(LoginPageLocators.footer)
    main_page.click(MainPageLocators.facebook_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_facebook == click_on_icon.current_url, "Actual URL is not the same as expected"


@pytest.mark.social_media
def test_social_media_linkedin_link(driver, valid_user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*valid_user_credentials)
    main_page.scroll_to_element(LoginPageLocators.footer)
    main_page.click(MainPageLocators.linkedin_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_linkedin == click_on_icon.current_url, "Actual URL is not the same as expected"


@pytest.mark.social_media
def test_social_media_twitter_link(driver, valid_user_credentials):
    main_page = UserInteractions(driver)
    main_page.open()
    main_page.login(*valid_user_credentials)
    main_page.scroll_to_element(LoginPageLocators.footer)
    main_page.click(MainPageLocators.twitter_icon)
    main_page.switch_to_window_by_index()
    click_on_icon = MainPage(driver)

    assert click_on_icon.expected_url_twitter == click_on_icon.current_url, "Actual URL is not the same as expected"
