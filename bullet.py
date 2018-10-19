from sprite import Sprite


class Bullet(Sprite):

    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.grid = '_'

    def add_bullet(self, matrix):
        matrix[self.position_x][self.position_y] = self.grid

    def remove_bullet(self, matrix):
        matrix[self.position_x][self.position_y] = ' '

    def move_bullet(self, matrix):
        self.remove_bullet(matrix)
        self.change_location(self.position_x, self.position_y + 6)
        if self.check_collision(matrix) == 0:
            self.add_bullet(matrix)
        else:
            self.remove_bullet(matrix)
            for i in range(1, 12):
                matrix[self.position_x][self.position_y + i] = ' '
                matrix[self.position_x + 1][self.position_y + i] = ' '

    def check_collision(self, matrix):
        for i in range(1, 12):
            if matrix[self.position_x][self.position_y + i] == ' ':
                return 0
            else:
                return 1


game_bullet = Bullet(0, 0)
