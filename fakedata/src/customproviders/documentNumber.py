
from faker.providers import BaseProvider
from src.my_project_utils import random_generator


# Our custom provider inherits from the BaseProvider
class DocumentNumbers(BaseProvider):
    @staticmethod
    def document_number(customer_account_number):
        rn = random_generator.RandomCustom()
        rl = random_generator.RandomCustom()

        return rn.random_number(3) + '-' + rl.random_letter(4) + '-' + customer_account_number + rl.random_letter(1)
