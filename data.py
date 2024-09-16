class TestAuthorizationData:
    CREATE_COURIER_BODY = {
        "password": "password",
        "firstName": "name"
    }

    LOGIN_COURIER_BODY = {
        "password": "password",
    }

class OrderData:
    order_data_template = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

class ErrorMessages:
    DUPLICATE_COURIER = "Этот логин уже используется. Попробуйте другой."
