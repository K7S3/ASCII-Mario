from sprite import Sprite

# the classs for mario, luigi, enemy
class Character(Sprite):

    def __init__(self, position_x, position_y):

        super().__init__(position_x, position_y)
        self.grid = []

    def add_character(self, matrix):

        for i in range(2):
            for j in range(4):
                matrix[self.position_x + i][self.position_y + j] = self.grid[i][j]

    def remove_character(self, matrix):

        for i in range(2):
            for j in range(4):
                matrix[self.position_x + i][self.position_y + j] = ' '

    def __check_obstacle(self, matrix, new_position_x, new_position_y):

        for i in range(2):
            for j in range(4):
                if matrix[new_position_x + i][new_position_y + j] == '/' or matrix[new_position_x + i][
                    new_position_y + j] == '0' or matrix[new_position_x + i][new_position_y + j] == '*':
                    return -1
                if matrix[new_position_x + i][new_position_y + j] == '<' or matrix[new_position_x + i][
                    new_position_y + j] == '|':
                    self.remove_character(matrix)
                    self.grid = []
                    return 1
        return 0

    def move_character(self, matrix, new_position_x, new_position_y):
        try:
            if self.__check_obstacle(matrix, new_position_x, new_position_y) == -1:
                return -1

            if self.__check_obstacle(matrix, new_position_x, new_position_y) == 1:
                return 1
            self.remove_character(matrix)

            self.change_location(new_position_x, new_position_y)
            self.add_character(matrix)
            return 0
        except:
            return -2
    def gravity(self, matrix):
        x = self.position_x
        y = self.position_y
        try:
            self.move_character(matrix, x + 2, y)
            return 0
        except:
            if x == 41:
                self.move_character(matrix, 44, y)
                return 0
            else:
                return 1
