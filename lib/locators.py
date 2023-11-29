from selenium.webdriver.common.by import By


class LoginPageLocators:
    url = "https://www.saucedemo.com"
    input_login = (By.XPATH, '//*[@id="user-name"]')
    input_password = (By.XPATH, '//*[@id="password"]')
    login_button = (By.XPATH, '//*[@id="login-button"]')


class LoggedInSuccessfullyLocators:
    url = "https://www.saucedemo.com/inventory.html"
    footer = (By.XPATH, '//*[@id="page_wrapper"]/footer/div')


class LoggedInUnsuccessfullyLocators:
    url = "https://www.saucedemo.com/"
    login_header = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')


class MainPageSocialMediaFacebookLocators:
    facebook_icon = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[2]/a')
    facebook_url = 'https://www.facebook.com/saucelabs'


class MainPageSocialMediaTwitterLocators:
    twitter_icon = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    twitter_url = 'https://twitter.com/saucelabs'


class MainPageSocialMediaLinkedInLocators:
    linkedin_icon = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[3]/a')
    linkedin_url = 'https://www.linkedin.com/company/sauce-labs/'
