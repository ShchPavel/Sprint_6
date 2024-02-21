import random
import string

from faker import Faker


class DataGenerator:
    fake = Faker('ru_RU')

    def get_random_name(self):
        return self.fake.first_name()

    def get_random_surname(self):
        return self.fake.last_name()

    def get_random_address(self):
        self.fake.city = 'Москва'
        return f'{self.fake.street_name()} {self.fake.numerify('##')}'

    def get_random_phone(self):
        return f'8{self.fake.numerify('##########')}'

    @staticmethod
    def get_random_comment():
        characters = string.ascii_letters.lower()
        return str(''.join(random.choice(characters) for _ in range(15)))