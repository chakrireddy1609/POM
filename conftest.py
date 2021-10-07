import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.demoblaze.com/")
    request.cls.driver = driver
    yield
    driver.close()