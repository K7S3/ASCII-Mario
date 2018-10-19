from sprite import Sprite

# The cloud class
class Cloud(Sprite):

    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.grid = []

    def add_cloud(self, matrix):
        for i in range(5):
            for j in range(5):
                matrix[self.position_x + i][self.position_y + j] = self.grid[i][j]


def add_floating_clouds(matrix):
    for i in range(1, 60):
        game_cloud = Cloud(4, 60 * i)
        game_cloud.grid = [[' ', ' ', ' ', ' ', ' '], [' ', '(', ' ', ')', ' '], ['(', ' ', ' ', ' ', ')'],
                           [' ', '(', ' ', ')', ' '], [' ', ' ', ' ', ' ', ' ']]
        game_cloud.add_cloud(matrix)
