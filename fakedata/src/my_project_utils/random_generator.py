import random

numeric_sample = '0123456789'


class RandomCustom:

    @staticmethod
    def random_seed(seed):
        random.seed(seed)

    @staticmethod
    def random_number(number_length):
        digits_sample = '0123456789'
        return ''.join(random.sample(digits_sample, number_length))

    @staticmethod
    def random_letter(number_length):
        chars_sample = 'ABCDEFGJIKLMNOPQRSTUVWXYZ'
        return ''.join(random.sample(chars_sample, number_length))

    @staticmethod
    def random_b_or_c():
        chars_sample = 'bc'
        return ''.join(random.sample(chars_sample, 1))

    @staticmethod
    def random_range(start, end, step=1):
        return random.randrange(start, end, step)

    # the lower the seed value, the less are the True returned
    def true_or_false_seeded(self, seed):
        control = self.random_number(1)
        if int(control) < seed:
            return True
        else:
            return False

    # the lower the seed value, the less are the True returned
    def one_or_two_seeded(self, seed):
        control = self.random_number(1)
        if int(control) < seed:
            return 1
        else:
            return 2
