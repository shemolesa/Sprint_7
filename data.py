URL = 'http://qa-scooter.praktikum-services.ru/'
URL_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
URL_COURIER_LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
URL_ORDERS = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'
TEST_COURIER = {
    "login": "me_test_courier",
    "password": "me_password",
    "firstName": "name_courier"
}
TEST_COURIER_INCORRECT_LOGIN = {
    "login": "me_test_courier_incorrect",
    "password": "me_password"
}
TEST_COURIER_INCORRECT_PASSWORD = {
    "login": "me_test_courier",
    "password": "me_password_incorrect"
}

TEST_ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}