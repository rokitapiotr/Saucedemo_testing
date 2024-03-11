import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as Safari


@pytest.fixture(params=["chrome", "firefox", "safari", "edge", "ie", "opera"])
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")

    match browser:
        case "chrome":
            my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        case "firefox":
            my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case "safari":
            my_driver = webdriver.Safari(service=Safari(GeckoDriverManager().install()))
        case "edge":
            my_driver = webdriver.Edge()
        case "ie":
            my_driver = webdriver.Ie()
        case "opera":
            my_driver = webdriver.Opera()
        case _:
            raise TypeError(f"Expected 'chrome', 'firefox', 'safari', 'edge', 'ie', or 'opera' but got {browser}")

    my_driver.maximize_window()
    my_driver.implicitly_wait(15)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome,firefox and Safari)"
    )


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request, driver):
    yield
    if request.node.rep_setup.passed and request.node.rep_call.failed:
        driver = request.node.funcargs['driver']
        take_screenshot(driver, request.node.nodeid)
        print("executing test failed", request.node.nodeid)


def take_screenshot(driver, node_id, sleep=3):
    time.sleep(sleep)
    file_name = f'{node_id}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot(file_name)
