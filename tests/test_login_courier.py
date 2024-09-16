import allure
import pytest
from helpers import TestDataHelper
from scooter_api import ScooterApi


class TestAuthorizationEndpoint:

    @allure.description("Проверка кода ответа и id для успешной авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Тест успешной авторизации курьера")
    def test_successful_login(self, generate_random_login, create_and_delete_user):
        login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
        assert login_response.status_code == 200 and 'id' in login_response.json()

    @allure.description("Проверка, что авторизация невозможна если передать только login")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Тест авторизации без пароля")
    def test_login_requires_only_login_bad_request(self, generate_random_login, create_and_delete_user):
        login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
        assert login_response.status_code == 200
        login_body = TestDataHelper.generate_login_body(generate_random_login)
        login_body.pop("login")
        incomplete_login_response = ScooterApi.login_courier(login_body)
        assert incomplete_login_response.status_code == 400

    @allure.description("Проверка, что при вводе неправильных логина или пароля система вернёт ошибку 404")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Тест авторизации с неверными данными")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_with_invalid_login_and_password(self, field, generate_random_login, create_and_delete_user):
        login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))
        assert login_response.status_code == 200
        login_body = TestDataHelper.generate_login_body(generate_random_login)
        login_body[field] = "new_value"
        incomplete_login_response = ScooterApi.login_courier(login_body)

        assert incomplete_login_response.status_code == 404

    @allure.description("Проверка, что авторизация под несуществующим пользователем вызывает ошибку 404")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Тест авторизации несуществующего пользователя")
    def test_login_with_nonexistent_user(self, create_and_delete_user):
        nonexistent_user_body = {
            "login": "nonexistent_user_login",
            "password": "nonexistent_user_password"
        }
        login_response = ScooterApi.login_courier(nonexistent_user_body)

        assert login_response.status_code == 404
