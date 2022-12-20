import pytest
from selenium.webdriver.common.by import By
from variables import login, WRONG_LOGIN, WRONG_LOGIN_IDS, WRONG_PASSWORDS, WRONG_PASSWORD_IDS, PASSWORD, EMAIL


# 8 негативных:
class TestNegativeAuth:
    @pytest.mark.parametrize("email", WRONG_LOGIN, ids=WRONG_LOGIN_IDS)
    def test_negative_login(self, email, password=PASSWORD):
        login(email, password)
        title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
        assert title == 'Авторизация'

    @pytest.mark.parametrize("password", WRONG_PASSWORDS, ids=WRONG_PASSWORD_IDS)
    def test_negative_password(self, password, email=EMAIL):
        login(email, password)
        title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
        assert title == 'Авторизация'

    def test_empty_fields(self, password='', email=''):
        login(email, password)
        title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
        assert title == 'Авторизация'
