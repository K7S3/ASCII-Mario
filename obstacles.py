import random

from brick import *

# adds random obstacles
def add_floating_bricks(matrix):
    for x in range(20):
        game_floating_brick.add_bricks(matrix, random.randint(2, 8) * 4, random.randint(2, 270) * 4,
                                       random.randint(8, 16))


def add_ground_bricks(matrix):
    for x in range(1, 10):
        for y in range(random.randint(2, 4)):
            game_ground_brick.add_bricks(matrix, 46 - y*2, 100 * x, random.randint(1, 3) * 4)
