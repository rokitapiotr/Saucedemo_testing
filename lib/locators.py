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
    login_accepted_usernames = (By.XPATH, '//*[@id="login_credentials"]/h4')
    login_accepted_passwords = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/h4')
