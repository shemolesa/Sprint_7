import requests
import pytest
import allure
import data
import json

class TestOrder:

    @allure.title('Проверка успешной регистрации заказа с разными вариантами цветов')
    @pytest.mark.parametrize('color', [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_registration_order_complete_data_successfully(self, color):
        data.TEST_ORDER["color"] = color # добавляем цвет самоката в тело запроса
        # отправляем запрос на регистрацию заказа и сохраняем ответ в переменную response
        print(json.dumps(data.TEST_ORDER))
        response = requests.post(data.URL_ORDERS, data=json.dumps(data.TEST_ORDER))
        print(json.dumps(data.TEST_ORDER))
        # проверяем, что заказ оформлен: статус 201 и есть трек заказа
        assert response.status_code == 201 and response.json()["track"]


    @allure.title('Проверка получения списка заказа')
    def test_getting_list_orders_successfully(self):
        # отправляем запрос на регистрацию заказа и сохраняем ответ в переменную response
        response = requests.get(data.URL_ORDERS)
        # проверяем, что список получен: статус 200 и список не пустой
        assert response.status_code == 200 and len(response.json()) > 0

