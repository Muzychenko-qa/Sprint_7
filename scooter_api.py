from urllib.parse import urljoin

import allure
import requests
import urls


class ScooterApi:
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, data=body)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        delete_url = urls.BASE_URL + urls.DELETE_ENDPOINT.format(id=courier_id)
        return requests.delete(delete_url)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data):
        return requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=order_data)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_order_list():
        return requests.get(urls.BASE_URL + urls.ORDER_ENDPOINT)
