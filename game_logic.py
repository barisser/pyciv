import world

world_map_x = 100
world_map_y = 100

def init():
    data = {}
    data['world'] = World.World(world_map_x, world_map_y)
