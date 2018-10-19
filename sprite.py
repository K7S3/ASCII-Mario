class Sprite:

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def change_location(self, new_position_x, new_position_y):
        self.position_x = new_position_x
        self.position_y = new_position_y
