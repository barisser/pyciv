import city
import commodity
import constants
import land
import population
import random
import util


class World:
    def __init__(self, mapx, mapy):
        self.mapx = mapx
        self.mapy = mapy
        self.cities = []
        self.init_map()

    def init_map(self):
        self.init_random_land()
        self.init_random_cities(10)

    def init_random_land(self):
        self.map = []

        for i in range(0, self.mapx):
            r = []
            for b in range(0, self.mapy):
                terrain = 0
                resources = []

                new_land = land.Land(i, b, terrain, resources)
                new_land.randomize_resources()

                r.append(new_land)
            self.map.append(r)

    def random_map_point(self):
        return (util.random_int(0, self.mapx), util.random_int(0, self.mapy))

    def init_random_cities(self, n):
        self.cities = []
        for i in range(0, n):
            p = self.random_map_point()

            random_population = population.Population(1311, 3)
            commodities = [100] * len(self.commodities)
            name = str(i) + "-city"
            new_city = city.City(name, p[0], p[1], random_population, commodities)
            self.cities.append(new_city)
