import random

from faker.providers import BaseProvider
from utils import random_generator


# Our custom provider inherits from the BaseProvider
class DocumentNumbers(BaseProvider):
    def document_number(self, customer_account_number):
        rn = random_generator.RandomCustom()
        rl = random_generator.RandomCustom()

        return rn.random_number(3) + '-' + rl.random_letter(4) + '-' + customer_account_number + rl.random_letter(1)
