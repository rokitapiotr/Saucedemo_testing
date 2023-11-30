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


class MainPageSelectLocators:
    select_name_price = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')


class MainPageSelectAtoZLocators:
    first_product_name = (By.XPATH, '//*[@id="item_4_title_link"]/div')


class MainPageSelectZtoALocators:
    first_product_name = (By.XPATH, '//*[@id="item_3_title_link"]/div')


class MainPageSelectLowToHighLocators:
    first_product_name = (By.XPATH, '//*[@id="item_2_title_link"]/div')


class MainPageSelectHighToLowLocators:
    first_product_name = (By.XPATH, '//*[@id="item_5_title_link"]/div')


class MainPageAddingButtonLocators:
    first_item_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    first_item_remove_button = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    second_item_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    second_item_remove_button = (By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
    third_item_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    third_item_remove_button = (By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    shopping_cart_counter = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
