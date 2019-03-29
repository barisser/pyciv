import math
import random


class Population:
    def __init__(self, n, per_capita_money):
        self.n = n
        self.per_capita_money = per_capita_money

    def randomize(self):
        self.n = random.randint(0, 10000)
        self.per_capita_money = random.random()*10

    def relative_demands(self, commodity_prices, commodity_supplies, commodity_objects):
        return -1
