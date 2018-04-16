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

    @staticmethod
    def bounding_box(tile1, tile2):
        ''' Return true if collision between 2 tiles '''
        if not tile1 or not tile2:
            return False
        tile1_left_x = tile1.position[0]
        tile1_right_x = tile1_left_x + MovingTile.DIMS[0]
        tile1_top_y = tile1.position[1]
        tile1_bot_y = tile1_top_y + MovingTile.DIMS[1]
        tile2_left_x = tile2.position[0]
        tile2_right_x = tile2_left_x + StationaryTile.DIMS[0]
        tile2_top_y = tile2.position[1]
        tile2_bot_y = tile2_top_y + StationaryTile.DIMS[1]
        if tile1_left_x < tile2_right_x and tile1_right_x > tile2_left_x and \
                tile1_top_y < tile2_bot_y and tile1_bot_y > tile2_top_y:
            return True
        return False

    def check_collision(self):
        ''' Return the stationary tile that the moving_tile collided with '''
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
            if MovingTile.bounding_box(self, tile):
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
            if MovingTile.bounding_box(self.world.player, new_wall):
                continue
            if MovingTile.bounding_box(self.world.enemy, new_wall):
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
            if MovingTile.bounding_box(self.world.player, new_food):
                continue
            if MovingTile.bounding_box(self.world.enemy, new_food):
                continue
            self.world.grid[new_food_row][new_food_col] = new_food
            self.world.food = new_food
            break