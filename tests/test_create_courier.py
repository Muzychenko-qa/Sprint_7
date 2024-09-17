import allure
import pytest

from data import ErrorMessages
from helpers import TestDataHelper
from scooter_api import ScooterApi


class TestCreateCourier:

    @allure.description("Проверка кода ответа и содержимого ответа для успешного создания курьера")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Тест успешного создания курьера")
    def test_successful_create_courier(self, generate_random_login, delete_user):
        response = ScooterApi.create_courier(TestDataHelper.generate_registration_body(generate_random_login))
        login_response = ScooterApi.login_courier(TestDataHelper.generate_login_body(generate_random_login))

        assert response.status_code == 201 and response.text == '{"ok":true}'



    @allure.description("Проверка, что нельзя создать двух одинаковых курьеров")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Тест создания дубликата курьера")
    def test_create_duplicate_courier_fails(self, generate_random_login, delete_user):
        user_body = TestDataHelper.generate_registration_body(generate_random_login)
        ScooterApi.create_courier(user_body)
        second_request = ScooterApi.create_courier(user_body)
        assert (second_request.status_code == 409
                and second_request.json()["message"] == ErrorMessages.DUPLICATE_COURIER)

    @allure.description("Проверка, что запрос с отсутствующим полем login или password возвращает ошибку")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Тест создания курьера с отсутствующим полем")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_login_fails(self, missing_field, generate_random_login, delete_user):
        user_body = TestDataHelper.generate_registration_body(generate_random_login)

        user_body_missing_field = user_body.pop(missing_field)
        request = ScooterApi.create_courier(user_body_missing_field)
        assert request.status_code == 400

    @allure.description("Проверка, что для создание курьера, нужно передать в ручку обязательные поля login и password")
    def test_successful_courier_creation_requires_all_mandatory_fields(self, generate_random_login, delete_user):
        user_body = TestDataHelper.generate_registration_body(generate_random_login)
        incomplete_user_body = {
            "password": user_body["password"],
            "firstName": user_body["firstName"]
        }
        request = ScooterApi.create_courier(incomplete_user_body)
        assert request.status_code == 400
        user_body = TestDataHelper.generate_registration_body(generate_random_login)
        user_body.pop("firstName")
        request = ScooterApi.create_courier(user_body)
        assert request.status_code == 201
