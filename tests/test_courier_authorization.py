import requests
import pytest
import allure
import data

class TestCourierAuthorization:

    @allure.title('Проверка успешной авторизации курьера с реальными данными')
    def test_authorization_courier_real_data_successfully(self, response_courier):
        # проверяем, что тестовый курьер залогинился: код = 200 и есть id
        assert response_courier[1].status_code == 200 and response_courier[1].json()['id']

    @allure.title('Проверка наличия пароля для авторизации курьера')
    def test_authorization_courier_incomplete_data_error504(self):
        payload = {"login": "login_courier"}
        # логинимся без указания пароля
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем, что авторизfция не выполнена: код = 504 и текст "Service unavailable"
        assert response.status_code == 504 and response.text == data.AUTHORIZATION_MESSAGE_504

    @allure.title('Проверка наличия логина для авторизации курьера')
    def test_authorization_courier_incomplete_data_error400(self):
        payload = {"password": "password_courier"}
        # логинимся без указания логина
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем что авторизация не выполнена: код = 400 и сообщение "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()['message'] == data.AUTHORIZATION_MESSAGE_400

    @allure.title('Проверка обработки авторизации курьера с несуществующей парой логин-пароль')
    @pytest.mark.parametrize('payload', [data.TEST_COURIER_INCORRECT_LOGIN, data.TEST_COURIER_INCORRECT_PASSWORD])
    def test_authorization_courier_null_couple_error404(self, payload):
        # логинимся с несуществующей парой логин-пароль
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем, что авторизация не выполнена: код = 404 и сообщение "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()['message'] == data.AUTHORIZATION_MESSAGE_404



