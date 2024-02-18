import random

from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(0, 80),
        salary=random.randint(1000, 10000),
        department=faker_en.job()[:24],
        email=faker_en.email(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
    )
