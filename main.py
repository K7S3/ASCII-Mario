import os
from matrix import Matrix
from obstacles import *
from border import game_border
from floor import game_floor
from mario import game_mario
from luigi import game_luigi
from enemy import *
from bullet import Bullet
from cloud import add_floating_clouds

os.system("clear")
os.system("xdg-open mario_classic.mp3")

rows, columns = 48, 7200
game_matrix = Matrix(rows, columns)

#adds scenery
def add_scenery(game_matrix):
    game_floor.add_all(game_matrix.grid, 3600)
    game_border.add_border(game_matrix.grid)
    add_floating_bricks(game_matrix.grid)
    add_ground_bricks(game_matrix.grid)
    add_floating_clouds(game_matrix.grid)

#main function
def main():
    add_scenery(game_matrix)
    no_of_players = input('\033[34m' + 'Welcome to Super Mario 1 player or 2 player: ')
    level = 1
    return_value1 = 0
    return_value2 = 0
    if no_of_players == '1':
        game_mario.add_character(game_matrix.grid)
        add_enemies(game_matrix.grid)
        game_bullet = Bullet(0, 0)

        while True:

            if return_value1 == -2 or game_mario.gravity(game_matrix.grid) == 1:
                print('\033[31m' + 'Game over for mario')
                game_mario.remove_character(game_matrix.grid)
                return 1

            game_border.add_border(game_matrix.grid)

            random_enemies(game_matrix.grid)
            game_bullet.move_bullet(game_matrix.grid)
            if game_matrix.renderer(600, level) == 1:
                level = level + 1

            return_value1 = game_mario.move_mario(game_matrix.grid)
            frame_no = int(game_mario.check_position())
            game_matrix.grid[5][15 + 120 * frame_no] = random_enemies(game_matrix.grid)
            game_matrix.grid[5][30 + 120 * frame_no] = level
            game_matrix.grid[5][45 + 120 * frame_no] = game_mario.lives
            if return_value1 == 1:
                return_value1 = 0
            elif return_value1 == 3:
                game_bullet = Bullet(game_mario.position_x, game_mario.position_y + 6)

    elif no_of_players == '2':
        game_mario.add_character(game_matrix.grid)
        game_luigi.add_character(game_matrix.grid)
        add_enemies(game_matrix.grid)
        game_bullet = Bullet(0, 0)
        while True:

            if return_value1 == -2:
                print('\033[31m' + 'Game over for mario')
                game_mario.remove_character(game_matrix.grid)
                return 1
            if return_value2 == -2:
                print('\033[31m' + 'Game over for luigi')
                game_luigi.remove_character(game_matrix.grid)
                return 2

            game_border.add_border(game_matrix.grid)
            random_enemies(game_matrix.grid)
            game_bullet.move_bullet(game_matrix.grid)
            game_mario.gravity(game_matrix.grid)
            game_luigi.gravity(game_matrix.grid)
            if game_matrix.renderer(600, level) == 1:
                level = level + 1
            return_value1 = game_mario.move_mario(game_matrix.grid)
            return_value2 = game_luigi.move_luigi(game_matrix.grid)
            frame_no = int(game_mario.check_position())
            game_matrix.grid[5][10 + 120 * frame_no] = random_enemies(game_matrix.grid)
            game_matrix.grid[5][20 + 120 * frame_no] = level
            game_matrix.grid[5][30 + 120 * frame_no] = game_mario.lives
            game_matrix.grid[5][40 + 120 * frame_no] = game_luigi.lives
            if return_value1 == 1:
                return_value1 = 0
            elif return_value1 == 3:
                game_bullet = Bullet(game_mario.position_x, game_mario.position_y + 6)

            elif return_value2 == 1:
                return_value2 = 0
            elif return_value2 == 3:
                game_bullet = Bullet(game_luigi.position_x, game_luigi.position_y + 6)

    else:
        print('Please choose 1 or 2 only!')


main()
