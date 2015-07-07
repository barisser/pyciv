class Commodity:
    def __init__(self, name, price_elasticity, price_base_demand):
        self.name = name
        self.price_elasticity = price_elasticity
        self.price_base_demand = price_base_demand



def init_commodities():
    c = {}
    c['food'] = Commodity('food', 0.01, 1.0)
    c['lumber'] = Commodity('lumber', 1.0, 3.0)
    return c
