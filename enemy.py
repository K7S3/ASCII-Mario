import random
from character import Character

# The enemy class
class Enemy(Character):

    def __init__(self, position_x, position_y, points):
        super().__init__(position_x, position_y)
        self.grid = [['>', '#', '#', '<'], ['>', '#', '#', '<']]
        self.points = points
        self.count = random.randint(4, 10)

    def random_movement(self, matrix, x, y):

        self.remove_character(matrix)
        if self.count > 1:
            try:
                self.move_character(matrix, self.position_x - x, self.position_y + y)
                self.count = self.count - 1
            except:
                self.remove_character(matrix)
                self.grid=[]
        elif self.count == 1:
            self.count = -random.randint(4, 10)
            self.add_character(matrix)

        elif self.count == -1:
            self.count = random.randint(4, 10)
            self.add_character(matrix)

        else:
            try:
                self.move_character(matrix, self.position_x + x, self.position_y - y)
                self.count = self.count + 1
            except:
                self.remove_character(matrix)
                self.grid=[]
        return 0


game_enemy = []


def add_enemies(matrix):
    for i in range(1, 14):
        game_enemy.append(Enemy(44, 80 * i, 100))
        game_enemy[i - 1].add_character(matrix)


def random_enemies(matrix):
    enemy_points = 0
    for i in range(1, 14):
        try:
            game_enemy[i - 1].random_movement(matrix, 0, 4)
            # game_enemy[i - 1].gravity(matrix)
        except:
            enemy_points = enemy_points + game_enemy[i-1].points
    return enemy_points