import commodity
import math


def demand(price, elasticity, base, per_capita_money):
    p = float(price) / per_capita_money
    r = base - elasticity * p
    if r < 0:
        r = 0
    return r


def relative_demands(prices, supplies, per_capita_money, divisor):
    d = []
    commodity_objects = constants.commodities
    for i in range(0, len(prices)):
        c = commodity_objects[i]
        r = demand(prices[i], c.price_elasticity, c.price_base_demand, per_capita_money) / divisor
        d.append(r)
    return d


def perturb_price(supply, supply_change, price, total_population):
