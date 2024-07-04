import requests
import pytest
import allure
import data


@allure.step('Регистрация нового тестового курьера с передачей его id и с последующим удалением')
@pytest.fixture()
def response_courier():
    # отправляем запрос на регистрацию тестового курьера и сохраняем ответ в переменную
    response_courier = requests.post(data.URL_COURIER, data.TEST_COURIER)
    # отправляем запрос на авторизацию тестового курьера и сохраняем ответ в переменную
    response_id_courier = requests.post(data.URL_COURIER_LOGIN, data.TEST_COURIER)
    # находим id курьера
    id_courier = response_id_courier.json()['id']
    yield response_courier, response_id_courier
    #удаляем тестового курьера
    response_delete = requests.delete(f'{data.URL_COURIER}/{id_courier}')


