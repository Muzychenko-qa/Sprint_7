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
def delete_user(generate_random_login):
    yield
    login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
    user_id = login_response.json()['id']
    ScooterApi.delete_courier(user_id)

@pytest.fixture(scope="function")
def create_and_delete_user(generate_random_login, delete_user):
    ScooterApi.create_courier(TestDataHelper.generate_registration_body(generate_random_login))
    yield

