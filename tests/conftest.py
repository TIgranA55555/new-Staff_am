import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
service_obj = Service(r'C:\Users\USER\Desktop\drivers\chromedriver.exe')


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == 'chrome':
        service_obj = Service(r'C:\Users\USER\Desktop\drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == 'firefox':
        service_obj = Service(r'C:\Users\USER\Desktop\drivers\geckodriver.exe')
        driver = webdriver.Firefox(service=service_obj, options=options)
    driver.implicitly_wait(20)
    driver.get('https://staff.am/en')
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
