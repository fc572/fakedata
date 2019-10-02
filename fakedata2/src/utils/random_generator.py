import random

numeric_sample = '0123456789'


class RandomCustom:
    def random_number(self, number_length):
        digits_sample = '0123456789'
        return ''.join(random.sample(digits_sample, number_length))

    def random_letter(self, number_length):
        chars_sample = 'ABCDEFGJIKLMNOPQRSTUVWXYZ'
        return ''.join(random.sample(chars_sample, number_length))

    def random_range(self, start, end, step=1):
        return random.randrange(start, end, step)

    # the lower the seed value, the less are the True returned
    def true_or_false_seeded(self, seed):
        control = self.random_number(1)
        if int(control) < seed:
            return True
        else:
            return False
