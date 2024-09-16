import random
import string

import allure
import pytest

from helpers import TestDataHelper
from scooter_api import ScooterApi


@pytest.fixture(scope="session")
@allure.step("Генерация случайного логина")
def generate_random_login():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(8))

@pytest.fixture(scope="function")
@allure.step("Удаление курьера после теста")
def delete_user(generate_random_login):
    yield
    login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
    if login_response.status_code == 200:
        user_id = login_response.json().get('id')
        if user_id:
            ScooterApi.delete_courier(user_id)

@pytest.fixture(scope="function")
@allure.step("Создание и удаление курьера")
def create_and_delete_user(generate_random_login):
    ScooterApi.create_courier(TestDataHelper.generate_registration_body(generate_random_login))
    yield
    login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
    user_id = login_response.json()['id']
    ScooterApi.delete_courier(user_id)
