import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driverChrome():
    pytest.driver = webdriver.Chrome("c:\\chromedriver\\chromedriver.exe")
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://b2c.passport.rt.ru')

    yield

    pytest.driver.quit()
