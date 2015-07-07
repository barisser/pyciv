import commodity

class City:
    def __init__(self, name, x, y, population, commodities):
        self.name = name
        self.x = x
        self.y = y
        self.population = population
        self.commodities = commodities  #dictionary where keys are commodity names

    def produce(self):

    def consume(self):

    def determine_prices(self):

    def lifecycle(self):
        self.grow()
        self.consume()
        self.produce()
        self.determine_prices()
