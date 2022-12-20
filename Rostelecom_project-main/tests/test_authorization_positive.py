import pytest
from selenium.webdriver.common.by import By
from variables import EMAIL, PASSWORD, PHONE, login


# 12 позитивных:
class TestAuthorisation:
    def test_login_by_email(self):
        login(EMAIL, PASSWORD)
        currentEmail = pytest.driver.find_elements(By.CLASS_NAME, 'user-contacts-item__value')[1].text
        assert currentEmail == EMAIL

    def test_login_by_phone(self):
        login(PHONE, PASSWORD)
        currentEmail = pytest.driver.find_elements(By.CLASS_NAME, 'user-contacts-item__value')[0].text
        assert currentEmail == PHONE

    def test_login_with_spaces(self):
        login(' ' + EMAIL + ' ', ' ' + PASSWORD + ' ')
        currentEmail = pytest.driver.find_elements(By.CLASS_NAME, 'user-contacts-item__value')[1].text
        assert currentEmail == EMAIL

    def test_login_register_sensitive(self):
        login(EMAIL.upper(), PASSWORD)
        currentEmail = pytest.driver.find_elements(By.CLASS_NAME, 'user-contacts-item__value')[1].text
        assert currentEmail == EMAIL

    def test_forgot_password(self):
        pytest.driver.find_element(By.ID, 'forgot_password').click()
        text = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
        assert text == 'Восстановление пароля'

    def test_vk_button(self):
        pytest.driver.find_element(By.ID, 'oidc_vk').click()
        assert pytest.driver.title == 'ВКонтакте | Вход'

    def test_ok_button(self):
        pytest.driver.find_element(By.ID, 'oidc_ok').click()
        assert pytest.driver.title == 'Одноклассники'

    def test_mail_button(self):
        pytest.driver.find_element(By.ID, 'oidc_mail').click()
        assert pytest.driver.title == 'Mail.Ru — Запрос доступа'

    def test_google_button(self):
        pytest.driver.find_element(By.ID, 'oidc_google').click()
        assert pytest.driver.title == 'Вход\xa0– Google Аккаунты'

    def test_ya_button(self):
        pytest.driver.find_element(By.ID, 'oidc_ya').click()
        assert pytest.driver.title == 'Авторизация'

    def test_kc_register_button(self):
        pytest.driver.find_element(By.ID, 'kc-register').click()
        text = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
        assert text == 'Регистрация'

    def test_support(self):
        pytest.driver.find_element(By.CLASS_NAME, 'omnichat-text').click()
        write_button = pytest.driver.find_element(By.CLASS_NAME, 'svelte-7fsc8m').text
        assert write_button == 'Написать'
