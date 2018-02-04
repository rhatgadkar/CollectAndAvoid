from keys import Keys
from tile import Tile
from world import World
from wall import Wall
from food import Food
from random import randint

class Player(Tile):
    VERT_SPEED = 2
    HORIZ_SPEED = 2

    def __init__(self, world):
        self.position = (100, 300)
        self.color = (0, 255, 0)
        self.world = world
        self.dead = False
        self.got_food = False

    def _bounding_box(self, tile):
        if tile == None:
            return False
        player_left_x = self.position[0]
        player_right_x = player_left_x + Tile.DIMS[0]
        player_top_y = self.position[1]
        player_bot_y = player_top_y + Tile.DIMS[1]
        tile_left_x = tile.position[0]
        tile_right_x = tile_left_x + Tile.DIMS[0]
        tile_top_y = tile.position[1]
        tile_bot_y = tile_top_y + Tile.DIMS[1]
        if player_left_x <= tile_right_x and \
                player_right_x >= tile_left_x and \
                player_top_y <= tile_bot_y and player_bot_y >= tile_top_y:
            return True
        return False

    def _check_collision(self):
        player_col = self.position[0] / Tile.DIMS[0]
        player_row = self.position[1] / Tile.DIMS[1]
        surrounding_row_cols = [(player_row, player_col),
                                (player_row, player_col - 1),
                                (player_row, player_col + 1),
                                (player_row - 1, player_col),
                                (player_row + 1, player_col),
                                (player_row - 1, player_col - 1),
                                (player_row + 1, player_col + 1),
                                (player_row + 1, player_col - 1),
                                (player_row - 1, player_col + 1)]
        current_collision = False
        for tile_row_col in surrounding_row_cols:
            tile_row = tile_row_col[0]
            tile_col = tile_row_col[1]
            if tile_row < 0 or tile_col < 0 or \
                    tile_row >= self.world.num_total_rows or \
                    tile_col >= self.world.num_total_cols:
                continue
            tile = self.world.grid[tile_row][tile_col]
            if self._bounding_box(tile):
                current_collision = True
                if isinstance(tile, Wall):
                    self.dead = True
                elif isinstance(tile, Food) and not self.got_food:
                    self.got_food = True
                    self.world.grid[tile_row][tile_col] = None
                    bot_row = self.world.num_total_rows - 1
                    right_col = self.world.num_total_cols - 1
                    while True:
                        new_wall_row = randint(0, bot_row)
                        new_wall_col = randint(0, right_col)
                        if self.world.grid[new_wall_row][new_wall_col] == None:
                            self.world.grid[new_wall_row][new_wall_col] = \
                                Wall(new_wall_row, new_wall_col)
                            break
                    while True:
                        new_food_row = randint(0, bot_row)
                        new_food_col = randint(0, right_col)
                        if self.world.grid[new_food_row][new_food_col] == None:
                            self.world.grid[new_food_row][new_food_col] = \
                                Food(new_food_row, new_food_col)
                            break
        if not current_collision:    
            self.got_food = False

    def do_something(self):
        self._check_collision()
        x, y = self.position
        if Keys.up:
            y -= Player.VERT_SPEED
        if Keys.down:
            y += Player.VERT_SPEED
        if Keys.left:
            x -= Player.HORIZ_SPEED
        if Keys.right:
            x += Player.HORIZ_SPEED
        self.position = (x, y)
