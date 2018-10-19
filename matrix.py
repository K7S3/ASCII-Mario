import os, time
from mario import game_mario


class Matrix():

    def __init__(self, rows, columns, default_character=' '):

        self.__rows = rows
        self.__columns = columns
        self.grid = [[default_character] * columns for i in range(rows)]

    def __start_game(self, level):
        frame_no = int(game_mario.check_position())
        if frame_no >= 5 * level:
            print('\033[32m'+ "You win:")
            print('\033[32m'+ 'Next level in 5 secs')
            time.sleep(5)
            return 1


    def renderer(self, fps, level):

        os.system('clear')
        time.sleep(1/fps)
        frame_no = int(game_mario.check_position())

        if self.__start_game(level) == 1:
            return 1
        for i in range(self.__rows):
            for j in range(120 * frame_no, 120 * (frame_no + 2)):
                print(self.grid[i][j], end='')
            print('\033[33m')
        return 0
    # def move_matrix(self,position_x):
    #     for i in range(self.rows):
    #         for()
