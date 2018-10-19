from sprite import Sprite


class Brick(Sprite):

    def __init__(self, brick_character, position_x=0, position_y=0):
        super().__init__(position_x, position_y)
        self.brick_character = brick_character
        self.group = [[brick_character] * 2 for i in range(2)]

    def add_bricks(self, matrix, position_x, position_y, number_of_bricks=1):
        for i in range(2):
            for j in range(2 * number_of_bricks):
                matrix[position_x + i][position_y + j] = self.brick_character


game_floating_brick = Brick('/')
game_ground_brick = Brick('*')
game_floor_brick = Brick('0')
game_water_brick = Brick('~')
game_pit_brick = Brick(' ')
