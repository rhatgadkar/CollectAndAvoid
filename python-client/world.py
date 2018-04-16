from stationary_tile import StationaryTile
from wall import Wall
from food import Food

class World:
    WORLD_DIMS = (400, 400)
    TOTAL_ROWS = WORLD_DIMS[1] / StationaryTile.DIMS[1]
    TOTAL_COLS = WORLD_DIMS[0] / StationaryTile.DIMS[0]
    BOT_ROW = TOTAL_ROWS - 1
    RIGHT_COL = TOTAL_COLS - 1

    def __init__(self, food_row, food_col):
        if food_row <= 0 or food_row >= World.TOTAL_ROWS - 1:
            raise RuntimeError('Invalid food_row')
        if food_col <= 0 or food_col >= World.TOTAL_COLS - 1:
            raise RuntimeError('Invalid food_col')
        self.grid = []
        for row in range(World.TOTAL_ROWS):
            col_list = [None] * World.TOTAL_COLS
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
        for col in range(World.TOTAL_COLS):
            self.grid[0][col] = Wall(0, col)
        # initialize bot row
        for col in range(World.TOTAL_COLS):
            self.grid[World.BOT_ROW][col] = Wall(World.RIGHT_COL, col)
        # initialize left col
        for row in range(1, World.BOT_ROW):
            self.grid[row][0] = Wall(row, 0)
        # initialize right col
        for row in range(1, World.BOT_ROW):
            self.grid[row][World.RIGHT_COL] = Wall(row, World.RIGHT_COL)
        # put food in specified row, col
        self.food = Food(food_row, food_col)
        self.grid[food_row][food_col] = self.food
