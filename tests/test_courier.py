import requests
import pytest
import allure
import data
import helpers

class TestCourier:

    @allure.title('Проверка успешной регистрации курьера с полным набором данных')
    def test_registration_courier_complete_data_successfully(self, response_courier):
        # проверяем успешную регистрацию
        assert response_courier[0].status_code == 201 and response_courier[0].json() == {'ok': True}

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
        assert response.status_code == 400 and response.json()['message'] == data.REGISTRATION_MESSAGE_400
