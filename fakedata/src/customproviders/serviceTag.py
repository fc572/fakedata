import random

from faker.providers import BaseProvider


# Our custom provider inherits from the BaseProvider
class TagsProvider(BaseProvider):
    def tag(self, tag_number):
        tags = ['AA', 'BB', 'CC', 'DD', 'EE', 'FC']
        tag_prefix = random.choice(tags)
        return tag_prefix + '-' + tag_number
