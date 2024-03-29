import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urls import *



@pytest.fixture(scope='function')
def driver():
    options = Options()
    driver = webdriver.Chrome()
    options.add_argument('--window-size = 1020,2040')
    driver.get(URL_HOME_PAGE)
    yield driver
    driver.quit()
