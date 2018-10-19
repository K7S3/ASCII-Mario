from character import Character
from input import _Getch, _GetchUnix


class luigi(Character):

    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.grid = [['|', ' ', ' ', ' '], ['|', '_', '_', '_']]
        self.lives = 1
        self.points = 0

    def move_luigi(self, matrix):

        '''Character read from input function'''

        getch = _Getch()
        key = getch()
        return_value = 0
        x = self.position_x
        y = self.position_y
        # Movement according to keys

        if key is '8':
            return_value = self.move_character(matrix, x - 4, y + 0)

        elif key is '5':
            return_value = self.move_character(matrix, x + 2, y + 0)

        elif key is '4':
            return_value = self.move_character(matrix, x + 0, y - 4)

        elif key is '6':
            return_value = self.move_character(matrix, x + 0, y + 4)

        elif key is '2':
            return_value = 3

        elif key is '7':
            return -2

        # If pressed 7 exit the game right there

        return return_value


game_luigi = luigi(44, 12)
