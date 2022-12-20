import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


EMAIL = 'testlearning@bk.ru'
PASSWORD = 'Q1w2e3r4!'
PHONE = '+7 936 619-99-07'

WRONG_LOGIN = ['', 'testlearning@mail.ru', '89366199900']
WRONG_LOGIN_IDS = ['empty email', 'wrong email', 'wrong phone number']
WRONG_PASSWORDS = ['', 'Q1w2e3r', PASSWORD.upper(), PASSWORD.lower()]
WRONG_PASSWORD_IDS = ['empty password', 'wrong password', 'register upper', 'register lower']


def login(name, password):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(name)

    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(password)

    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, 'kc-login')))
    pytest.driver.find_element(By.ID, 'kc-login').click()
