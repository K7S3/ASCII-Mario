from mario import game_mario

# The border class
class Border:

    def __init__(self, border_character='^'):
        self.border_character = border_character

    def add_border(self, matrix):
        frame_no = int(game_mario.check_position())
        for i in range(1200):
            matrix[0][i] = self.border_character
        for i in range(46):
            matrix[i][120 * frame_no] = self.border_character

            matrix[i][120 * (frame_no + 1) - 1] = ' '
            matrix[i][120 * (frame_no - 1)] = ' '

            matrix[i][120 * (frame_no + 2) - 1] = self.border_character


game_border = Border()
