from stationary_tile import StationaryTile
from wall import Wall
from food import Food

class World:
    WORLD_DIMS = (400, 400)
    TOTAL_ROWS = WORLD_DIMS[1] / StationaryTile.DIMS[1]
    TOTAL_COLS = WORLD_DIMS[0] / StationaryTile.DIMS[0]
    BOT_ROW = TOTAL_ROWS - 1
    RIGHT_COL = TOTAL_COLS - 1
    NUM_SUBWORLD_ROWS = 5
    NUM_SUBWORLD_COLS = 5

    class SubWorld:
        def __init__(self, row_range, col_range):
            self.row_range = row_range
            self.col_range = col_range
            self.left_bound = []
            self.right_bound = []
            self.top_bound = []
            self.bot_bound = []

        def initialize_bounds(self, world):
            ''' append empty tiles to bounds '''
            self.left_bound = []
            self.right_bound = []
            self.top_bound = []
            self.bot_bound = []
            for row in self.row_range:
                if not world.grid[row][self.col_range[0]]:
                    self.left_bound.append((row, self.col_range[0]))
                if not world.grid[row][self.col_range[-1]]:
                    self.right_bound.append((row, self.col_range[-1]))
            for col in self.col_range:
                if not world.grid[self.row_range[0]][col]:
                    self.top_bound.append((self.row_range[0], col))
                if not world.grid[self.row_range[-1]][col]:
                    self.bot_bound.append((self.row_range[-1], col))
        
        def is_valid_row_col(self, row, col):
            return (row in self.row_range and col in self.col_range)

    def __init__(self, food_row, food_col):
        self.player = None
        self.enemy = None
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
        # create SubWorlds
        self.subworlds = []
        '''
        Each SubWorld has 5 rows and 5 cols

        SW0  SW1  SW2  SW3
        SW4  SW5  SW6  SW7
        SW8  SW9  SW10 SW11
        SW12 SW13 SW14 SW15
        '''
        row_iter = 0
        col_iter = 0
        while row_iter < World.TOTAL_ROWS:
            col_iter = 0
            while col_iter < World.TOTAL_COLS:
                row_range = range(row_iter, row_iter + World.NUM_SUBWORLD_ROWS)
                col_range = range(col_iter, col_iter + World.NUM_SUBWORLD_COLS)
                new_world = World.SubWorld(row_range, col_range)
                new_world.initialize_bounds(self)
                self.subworlds.append(new_world)
                col_iter += (World.NUM_SUBWORLD_COLS)
            row_iter += (World.NUM_SUBWORLD_ROWS)

    def set_player(self, player):
        self.player = player
    
    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_current_subworld(self, row, col):
        for subworld in self.subworlds:
            if row in subworld.row_range and col in subworld.col_range:
                return subworld
        return None
