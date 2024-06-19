import os
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
        mobile=faker_en.msisdn(),
        date_of_birth=faker_en.date_between(start_date='-30y', end_date='today').strftime('%d %B %Y'),
    )


def generated_file():
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(current_dir, f'filetest_{random.randint(1, 999)}.txt')
    file = open(file_path, 'w+')
    file.write(f"Test {random.randint(1, 500)}")
    file.close()
    return file.name, file_path
