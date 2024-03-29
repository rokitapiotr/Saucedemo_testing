from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, text: str, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).send_keys(text)

    def click(self, locator: tuple, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).click()

    def wait_until_element_is_visible(self, locator: tuple, time: int = 25):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def select_div_by_value(self, locator: tuple, option_value: str, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        select_element = Select(self.find(locator))
        select_element.select_by_value(option_value)

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def open_url(self, url: str):
        self.driver.get(url)

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def get_text(self, locator: tuple, time: int = 25) -> str:
        self.wait_until_element_is_visible(locator, time)
        return self.find(locator).text

    def scroll_to_element(self, locator: tuple, time: int = 25):
        self.wait_until_element_is_visible(locator, time)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_window_by_index(self, index: int = 1, time: int = 25):
        wait = WebDriverWait(self.driver, time)
        wait.until(lambda driver: len(self.driver.window_handles) > index)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])
