import os
import random


def random_int(start, end):
    random.seed(random.randint(0, 1000000))
    return random.randint(start, end)
