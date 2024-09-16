import pytest
import allure
from scooter_api import ScooterApi
from data import OrderData


class TestOrder:

    @allure.description("Создание заказа с разными вариантами цвета")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Тест создания заказа с различными цветами")
    @pytest.mark.parametrize("colors", [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]), ([])])
    def test_create_order_with_different_colors(self, colors):
        order_data = OrderData.order_data_template.copy()
        order_data["color"] = colors
        response = ScooterApi.create_order(order_data)

        assert response.status_code == 201

    @allure.description("Проверка наличия ключа 'track' в ответе при создании заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Тест ответа на создание заказа: проверка наличия ключа 'track'")
    def test_create_order_response_contains_track(self):
        order_data = OrderData.order_data_template.copy()
        order_data["color"] = ["BLACK"]
        response = ScooterApi.create_order(order_data)
        response_body = response.json()
        assert "track" in response_body

    @allure.description("Проверка получения списка заказов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Тест получения списка заказов")
    def test_get_order_list(self):
        response = ScooterApi.get_order_list()

        assert response.status_code == 200
        response_body = response.json()
        assert "orders" in response_body and isinstance(response_body["orders"], list)
