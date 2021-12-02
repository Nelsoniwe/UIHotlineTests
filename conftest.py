import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(executable_path="./chromedriver")
#     yield driver
#     driver.quit()

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()