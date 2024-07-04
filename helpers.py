import allure
import random
import string



@allure.step('Генерация данных курьера для регистрации')
def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

