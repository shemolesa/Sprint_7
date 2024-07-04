URL = 'http://qa-scooter.praktikum-services.ru/'
URL_COURIER = URL + 'api/v1/courier'
URL_COURIER_LOGIN = URL + 'api/v1/courier/login'
URL_ORDERS = URL + 'api/v1/orders'
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

REGISTRATION_MESSAGE_409 = 'Этот логин уже используется. Попробуйте другой.'
REGISTRATION_MESSAGE_400 = "Недостаточно данных для создания учетной записи"
AUTHORIZATION_MESSAGE_400 = "Недостаточно данных для входа"
AUTHORIZATION_MESSAGE_404 = "Учетная запись не найдена"
AUTHORIZATION_MESSAGE_504 = "Service unavailable"