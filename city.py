import commodity
import constants
import economics


class City:
    def __init__(self, name, x, y, population, commodities):
        self.name = name
        self.x = x
        self.y = y
        self.population = population
        self.commodities = commodities  #array
        self.prices = [1] * len(commodities)

    def produce(self):
        return -1

    def consume(self):
        for i in range(0, constants.demand_steps_calculations):
            b = economics.relative_demands(self.prices, self.commodities)

    def update_prices(self):  #prices wont be 'determined' they will be like a dampened stochastic oscillator
                                # population demand will follow linear elastic model vs price
                                # supply will follow price
                                # price will be dampened state variable that is usually out of equilibrium
        return -1

    def lifecycle(self):
        self.grow()
        self.consume()
        self.produce()
        self.update_prices()
