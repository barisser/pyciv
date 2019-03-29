import commodity
import random


class Land:
    def __init__(self, x, y, terrain_index, resources):
        self.x = x
        self.y = y
        self.terrain_index = terrain_index
        self.resources = resources

    def randomize_resources(self):
        for i in range(0, len(self.resources)):
            self.resources[i] = random.random()
