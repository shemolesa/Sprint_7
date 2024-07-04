# Sprint_7

## conftest.py 
фикстуры
_response_courier_ - регистрация тестового курьера с последующим удалением
_response_id_courier_ - регистрация тестового курьера и его авторизация с последующим удалением

## data.py
тестовые данные

## requirements.txt
внешние зависимости

## helpers.py
вспомогательные функции
_generate_string_ - генерация строки (логин/пароль/имя)


## test_courier.py
 тесты действий с курьером
_test_registration_courier_complete_data_successfully_ - Проверка успешной регистрации курьера
_test_registration_courier_double_error_ - Проверка невозможности регистрации курьера с повторяющимся логином
_test_registration_courier_incomplete_data_error_ - Проверка невозможности регистрации курьера с неполными обязательными полями
_test_authorization_courier_incomplete_data_error504_ - Проверка наличия пароля для авторизации курьера

## test_courier_authorization.py
_test_authorization_courier_real_data_successfully_ - Проверка успешной авторизации курьера
_test_authorization_courier_incomplete_data_error400_ - Проверка наличия логина для авторизации курьера
_test_authorization_courier_null_couple_error404_ - Проверка обработки авторизации курьера с несуществующей парой логин-пароль


## test_order.py
тесты действий с заказами
_test_registration_order_complete_data_successfully_ - Проверка успешной регистрации заказа с разными вариантами цветов
_test_registration_order_complete_data_successfully_ - Проверка получения списка заказа

