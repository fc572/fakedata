import random

from faker.providers import BaseProvider


# Our custom provider inherits from the BaseProvider
class BandwidthProvider(BaseProvider):
    @staticmethod
    def bandwidth():
        speeds = ["56 kbps", "1.5 Mbps", "4 Mbps", "10 Mbps", "100 Mbps", "600 Mbps", "1 Mbps",
                  "5 Mbps", "10 Mbps", "100 Gbps"]

        # We select a random destination from the list and return it
        return random.choice(speeds)
