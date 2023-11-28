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
    header = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
