from tile import Tile
from wall import Wall
from food import Food
from random import randint

class World:
    WORLD_DIMS = (400, 400)

    def __init__(self):
        self.grid = []
        self.num_total_rows = World.WORLD_DIMS[1] / Tile.DIMS[1]
        self.num_total_cols = World.WORLD_DIMS[0] / Tile.DIMS[0]
        for row in range(self.num_total_rows):
            col_list = [None] * self.num_total_cols
            self.grid.append(col_list)
        '''
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        # initialize top row
        right_col = self.num_total_cols - 1
        bot_row = self.num_total_rows - 1
        for col in range(self.num_total_cols):
            self.grid[0][col] = Wall(0, col)
        # initialize bot row
        for col in range(self.num_total_cols):
            self.grid[bot_row][col] = Wall(right_col, col)
        # initialize left col
        for row in range(1, bot_row):
            self.grid[row][0] = Wall(row, 0)
        # initialize right col
        for row in range(1, bot_row):
            self.grid[row][right_col] = Wall(row, right_col)
        # put food in random row, col
        food_row = randint(1, self.num_total_rows - 2)
        food_col = randint(1, self.num_total_cols - 2)
        self.grid[food_row][food_col] = Food(food_row, food_col)
