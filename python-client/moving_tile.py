from world import World
from tile import Tile
from wall import Wall
from food import Food
from stationary_tile import StationaryTile
from random import randint

class MovingTile(Tile):
    VERT_SPEED = 2
    HORIZ_SPEED = 2
    DIMS = (15, 15)

    def __init__(self, world):
        self.world = world
        self.got_food = False

    def bounding_box(self, tile):
        ''' Return true if collision between specified tile and moving_tile '''
        if tile == None:
            return False
        moving_tile_left_x = self.position[0]
        moving_tile_right_x = moving_tile_left_x + MovingTile.DIMS[0]
        moving_tile_top_y = self.position[1]
        moving_tile_bot_y = moving_tile_top_y + MovingTile.DIMS[1]
        tile_left_x = tile.position[0]
        tile_right_x = tile_left_x + StationaryTile.DIMS[0]
        tile_top_y = tile.position[1]
        tile_bot_y = tile_top_y + StationaryTile.DIMS[1]
        if moving_tile_left_x < tile_right_x and \
                moving_tile_right_x > tile_left_x and \
                moving_tile_top_y < tile_bot_y and \
                moving_tile_bot_y > tile_top_y:
            return True
        return False

    def check_collision(self):
        ''' Return the tile that the moving_tile collided with '''
        moving_tile_col = self.position[0] / StationaryTile.DIMS[0]
        moving_tile_row = self.position[1] / StationaryTile.DIMS[1]
        surrounding_row_cols = [(moving_tile_row, moving_tile_col),
                                (moving_tile_row, moving_tile_col - 1),
                                (moving_tile_row, moving_tile_col + 1),
                                (moving_tile_row - 1, moving_tile_col),
                                (moving_tile_row + 1, moving_tile_col),
                                (moving_tile_row - 1, moving_tile_col - 1),
                                (moving_tile_row + 1, moving_tile_col + 1),
                                (moving_tile_row + 1, moving_tile_col - 1),
                                (moving_tile_row - 1, moving_tile_col + 1)]
        for tile_row_col in surrounding_row_cols:
            tile_row = tile_row_col[0]
            tile_col = tile_row_col[1]
            if tile_row < 0 or tile_col < 0 or \
                    tile_row >= World.TOTAL_ROWS or \
                    tile_col >= World.TOTAL_COLS:
                continue
            tile = self.world.grid[tile_row][tile_col]
            if self.bounding_box(tile):
                return tile
        return None

    def add_new_wall(self):
        # add new wall tile in location not continaining any tile
        while True:
            new_wall_row = randint(0, World.BOT_ROW)
            new_wall_col = randint(0, World.RIGHT_COL)
            new_wall = Wall(new_wall_row, new_wall_col)
            if self.world.grid[new_wall_row][new_wall_col] != None:
                continue
            if MovingTile.bounding_box(self, new_wall):
                continue
            self.world.grid[new_wall_row][new_wall_col] = new_wall
            break

    def add_new_food(self):
        # add new food tile in location not continaining any tile
        while True:
            new_food_row = randint(0, World.BOT_ROW)
            new_food_col = randint(0, World.RIGHT_COL)
            new_food = Food(new_food_row, new_food_col)
            if self.world.grid[new_food_row][new_food_col] != None:
                continue
            if self.bounding_box(new_food):
                continue
            self.world.grid[new_food_row][new_food_col] = new_food
            self.world.food = new_food
            break