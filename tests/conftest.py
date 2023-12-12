from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import pytest

from PageObjects.homepage import HomePage

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()