from character import Character
from input import _Getch, _GetchUnix


class Mario(Character):

    def __init__(self, position_x, position_y):

        super().__init__(position_x, position_y)
        self.grid = [['|', '\\', '/', '|'], ['|', ' ', ' ', '|']]
        self.lives = 1
        self.points = 0

    def move_mario(self, matrix):

        '''Character read from input function'''

        getch = _Getch()
        key = getch()
        return_value = 0
        x = self.position_x
        y = self.position_y
        # Movement according to keys
        if key is 'w':
            return_value = self.move_character(matrix, x - 4, y + 0)

        elif key is 's':
            return_value = self.move_character(matrix, x + 2, y + 0)

        elif key is 'a':
            return_value = self.move_character(matrix, x + 0, y - 4)

        elif key is 'd':
            return_value = self.move_character(matrix, x + 0, y + 4)

        elif key is 'x':
            return_value = 3

        elif key is 'q':
            return -2

        # If pressed q exit the game right there

        return return_value

    def check_position(self):
        return self.position_y / 120


game_mario = Mario(44, 24)
