import random

from faker.providers import BaseProvider
from utils import random_generator


# Our custom provider inherits from the BaseProvider
class SerialNumbers(BaseProvider):
    def serial_number(self):
        rn = random_generator.RandomCustom()
        rl = random_generator.RandomCustom()
        if random.randint(1, 10) % 2 == 0:
            return rl.random_letter(2) + '-' + rn.random_number(7)
        else:
            return rl.random_letter(3) + rn.random_number(8)
