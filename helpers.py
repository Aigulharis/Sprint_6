import pytest
from faker import Faker
import random

stations = ["Киевская", "Пушкинская", "Арбатская", "Комсомольская", "Сокольники"]
dataset = ['25.05.2025', '28.05.2025']

faker = Faker('ru_RU')
def generate_fill_personal_info():
    name = faker.first_name()
    last_name = faker.last_name()
    phone = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    street = faker.street_name()
    house_number = faker.building_number()
    address = f"{street}, д. {house_number}"
    metro = random.choice(stations)
    date = random.choice(dataset)
    comment = "# " + faker.sentence()
    return name, last_name, address, phone, metro, date, comment  # Возвращаем кортеж
