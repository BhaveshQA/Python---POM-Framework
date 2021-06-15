"""
common generic settings files
"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        path = r"F:\ProfessionSkillImprovement\PythonSeleniumFramework\browser\chromedriver.exe"
        # testURL = "https://rahulshettyacademy.com/angularpractice/shop"
        # ChromeOptions() class used for the settings
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_experimental_option("useAutomationExtension", False)
        chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Invoke the chrome browser
        driver = webdriver.Chrome(executable_path=path, options=chrome_option)
        # assign the local driver reference to the driver object
    elif browser_name == 'firefox':
        path = r"F:\ProfessionSkillImprovement\PythonSeleniumFramework\browser\geckodriver.exe."
        driver = webdriver.Firefox(executable_path=path)

    request.cls.driver = driver

    yield
    driver.quit()
