from world import World
from tile import Tile
from stationary_tile import StationaryTile

class MovingTile(Tile):
    VERT_SPEED = 2
    HORIZ_SPEED = 2
    DIMS = (15, 15)

    def __init__(self, world):
        self.world = world
        self.got_food = False

    def get_got_food(self):
        return self.got_food

    def set_got_food(self, value):
        self.got_food = value

    def _bounding_box(self, tile):
        ''' Return true if collision between specified tile and moving_tile '''
        if tile == None:
            return False
        moving_tile_left_x = self.position[0]
        moving_tile_right_x = moving_tile_left_x + MovingTile.DIMS[0]
        moving_tile_top_y = self.position[1]
        moving_tile_bot_y = moving_tile_top_y + MovingTile.DIMS[1]
        tile_left_x = tile.position[0]
        tile_right_x = tile_left_x + MovingTile.DIMS[0]
        tile_top_y = tile.position[1]
        tile_bot_y = tile_top_y + MovingTile.DIMS[1]
        if moving_tile_left_x < tile_right_x and \
                moving_tile_right_x > tile_left_x and \
                moving_tile_top_y < tile_bot_y and \
                moving_tile_bot_y > tile_top_y:
            return True
        return False

    def _check_collision(self):
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
            if self._bounding_box(tile):
                return tile, tile_row, tile_col
        return None