from brick import *
import random

# Floor class inherited from brick
class Floor(Brick):

    def __init__(self, position_x, position_y):

        super().__init__(self)
        self.position_x = position_x
        self.position_y = position_y

    def __add_floor(self, matrix, number_of_bricks):
        game_floor_brick.add_bricks(matrix, self.position_x, self.position_y, number_of_bricks)

    def __add_water(self, matrix):
        for x in range(10):
            game_water_brick.add_bricks(matrix, 46, random.randint(8, 270) * 4,
                                        random.randint(2, 4))

    def __add_pits(self, matrix):
        for x in range(5):
            game_pit_brick.add_bricks(matrix, 46, random.randint(8, 270) * 4,
                                      random.randint(4, 8))

    def add_all(self, matrix, number_of_bricks):
        self.__add_floor(matrix,number_of_bricks)
        self.__add_water(matrix)
        self.__add_pits(matrix)

game_floor = Floor(46, 0)
