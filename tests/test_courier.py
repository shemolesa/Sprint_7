import requests
import pytest
import allure
import data
import helpers

class TestCourier:

    @allure.title('Проверка успешной регистрации курьера с полным набором данных')
    def test_registration_courier_complete_data_successfully(self, response_courier):
        # проверяем успешную регистрацию
        assert response_courier.status_code == 201 and response_courier.json() == {'ok': True}

    @allure.title('Проверка невозможности регистрации курьера с повторяющимся логином')
    def test_registration_courier_double_error(self, response_courier): #передаем
        # отправляем запрос на регистрацию курьера с повторяющимся логином и сохраняем ответ в переменную response
        response = requests.post(data.URL_COURIER, data.TEST_COURIER)
        # проверяем, что курьер не зарегистрирован, выдалось соответствующее сообщение
        assert response.status_code == 409 and response.json()['message'] == data.REGISTRATION_MESSAGE_409


    @allure.title('Проверка невозможности регистрации курьера с неполными обязательными полями')
    @pytest.mark.parametrize('payload', [{"login": helpers.generate_string(6), "firstName": 'first_name_q'},
                                         {"password": helpers.generate_string(6), "firstName": 'first_name_q'}])
    def test_registration_courier_incomplete_data_error(self, payload):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(data.URL_COURIER, data=payload)
        # проверяем, что курьер не зарегистрирован, выдалось соответствующее сообщение
        assert response.status_code == 400 and response.json()['message'] == data.REGISTRATION_MESSAGE_400 #"Недостаточно данных для создания учетной записи"

    @allure.title('Проверка успешной авторизации курьера с реальными данными')
    def test_authorization_courier_real_data_successfully(self, response_id_courier):
        # проверяем, что тестовый курьер залогинился: код = 200 и есть id
        assert response_id_courier.status_code == 200 and response_id_courier.json()['id']

    @allure.title('Проверка наличия пароля для авторизации курьера')
    def test_authorization_courier_incomplete_data_error504(self):
        payload = {"login": "login_courier"}
        # логинимся без указания пароля
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем, что авторизfция не выполнена: код = 504 и текст "Service unavailable"
        assert response.status_code == 504 and response.text == "Service unavailable"

    @allure.title('Проверка наличия логина для авторизации курьера')
    def test_authorization_courier_incomplete_data_error400(self):
        payload = {"password": "password_courier"}
        # логинимся без указания логина
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем что авторизация не выполнена: код = 400 и сообщение "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()['message'] == data.AUTHORIZATION_MESSAGE_400 #"Недостаточно данных для входа"

    @allure.title('Проверка обработки авторизации курьера с несуществующей парой логин-пароль')
    @pytest.mark.parametrize('payload', [data.TEST_COURIER_INCORRECT_LOGIN, data.TEST_COURIER_INCORRECT_PASSWORD])
    def test_authorization_courier_null_couple_error404(self, payload):
        # логинимся с несуществующей парой логин-пароль
        response = requests.post(data.URL_COURIER_LOGIN, data=payload)
        # проверяем, что авторизация не выполнена: код = 404 и сообщение "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()['message'] == data.AUTHORIZATION_MESSAGE_404 # "Учетная запись не найдена"


