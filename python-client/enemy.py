from stationary_tile import StationaryTile
from moving_tile import MovingTile
from world import World
from wall import Wall
from food import Food
from random import randint

class Enemy(MovingTile):
    STARTING_COL = 5
    STARTING_ROW = 5
    STARTING_X = STARTING_COL * StationaryTile.DIMS[0]
    STARTING_Y = STARTING_ROW * StationaryTile.DIMS[1]

    def __init__(self, world):
        super(self.__class__, self).__init__(world)
        self.position = (Enemy.STARTING_X, Enemy.STARTING_Y)
        self.color = (0, 0, 255)
        self.shortest_path = []
        self.food = self.world.food
        self._set_shortest_path(Enemy.STARTING_ROW, Enemy.STARTING_COL,
                                self.food.row, self.food.col)
        self.world.set_enemy(self)

    def do_something(self):
        x, y = self.position
        col = x / StationaryTile.DIMS[0]
        row = y / StationaryTile.DIMS[1]
        if self.world.food.row != self.food.row and \
                self.world.food.col != self.food.col:
            # food location updated, so set a new shortest_path
            self.food = self.world.food
            self._set_shortest_path(row, col, self.food.row, self.food.col)
        if not self.shortest_path:
            return
        next_tile = self.shortest_path[0]
        next_tile_x = next_tile.col * StationaryTile.DIMS[1]
        next_tile_y = next_tile.row * StationaryTile.DIMS[0]
        if x < next_tile_x:
            x += MovingTile.HORIZ_SPEED
        elif x > next_tile_x:
            x -= MovingTile.HORIZ_SPEED
        elif y < next_tile_y:
            y += MovingTile.VERT_SPEED
        elif y > next_tile_y:
            y -= MovingTile.VERT_SPEED
        else:
            self.shortest_path.pop(0)
        self.position = (x, y)
        collided_tile = MovingTile.check_collision(self)
        if collided_tile:
            if isinstance(collided_tile, Food):
                self.shortest_path = []
                self.world.grid[collided_tile.row][collided_tile.col] = None
                self.add_new_wall()
                self.add_new_food()

    class TilePath:
        def __init__(self, row, col, parent):
            self.row = row
            self.col = col
            self.parent = parent

        def get_path(self):
            root_tile = self
            to_return = []
            while root_tile:
                to_return.insert(0, root_tile)
                root_tile = root_tile.parent
            return to_return

    def _set_shortest_path(self, src_row, src_col, dst_row, dst_col):
        if src_row == dst_row and src_col == dst_col:
            self.shortest_path = []
            return
        start_tile = Enemy.TilePath(src_row, src_col, None)
        undiscovered_tiles = [start_tile]
        discovered_tiles = []
        for row in range(World.TOTAL_ROWS):
            col_list = [None] * World.TOTAL_COLS
            discovered_tiles.append(col_list)
        while undiscovered_tiles:
            curr_tile = undiscovered_tiles.pop(0)
            discovered_tiles[curr_tile.row][curr_tile.col] = curr_tile
            if curr_tile.row == dst_row and curr_tile.col == dst_col:
                self.shortest_path = curr_tile.get_path()
                return
            if curr_tile.row - 1 >= 0:
                up_tile = self.world.grid[curr_tile.row - 1][curr_tile.col]
                if not discovered_tiles[curr_tile.row - 1][curr_tile.col]:
                    if (not up_tile) or (up_tile and not \
                            isinstance(up_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row - 1, curr_tile.col,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.row + 1 < World.TOTAL_ROWS:
                down_tile = self.world.grid[curr_tile.row + 1][curr_tile.col]
                if not discovered_tiles[curr_tile.row + 1][curr_tile.col]:
                    if (not down_tile) or (down_tile and not \
                            isinstance(down_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row + 1, curr_tile.col,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.col - 1 >= 0:
                left_tile = self.world.grid[curr_tile.row][curr_tile.col - 1]
                if not discovered_tiles[curr_tile.row][curr_tile.col - 1]:
                    if (not left_tile) or (left_tile and not \
                            isinstance(left_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row, curr_tile.col - 1,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.col + 1 < World.TOTAL_COLS:
                right_tile = self.world.grid[curr_tile.row][curr_tile.col + 1]
                if not discovered_tiles[curr_tile.row][curr_tile.col + 1]:
                    if (not right_tile) or (right_tile and not \
                            isinstance(right_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row, curr_tile.col + 1,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
        self.shortest_path = []
        return