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
        self.food = self.world.food
        self.shortest_path = self._get_new_path(Enemy.STARTING_ROW,
                                                Enemy.STARTING_COL,
                                                self.food.row, self.food.col)
        self.world.set_enemy(self)

    def do_something(self):
        x, y = self.position
        col = x / StationaryTile.DIMS[0]
        row = y / StationaryTile.DIMS[1]
        if self.world.food.row != self.food.row or \
                self.world.food.col != self.food.col:
            # food location updated, so set a new shortest_path
            self.food = self.world.food
            for subworld in self.world.subworlds:
                subworld.reset_bounds(self.world)
            self.shortest_path = self._get_new_path(row, col, self.food.row,
                                                    self.food.col)
        if not self.shortest_path:
            # reached a destination, set new shortest path toward food
            self.shortest_path = self._get_new_path(row, col, self.food.row,
                                                    self.food.col)
            if not self.shortest_path:
                import pdb; pdb.set_trace()
                self.shortest_path = self._get_new_path(row, col, self.food.row,
                                                    self.food.col)
                # no shortest path found for new destination
                print 'hello1'
                print 'self.world.food.row: %d, self.world.food.col: %d' % (self.world.food.row, self.world.food.col)
                print 'self.food.row: %d, self.foodl.col: %d' % (self.food.row, self.food.col)
                subworld = self.world.get_current_subworld(row, col)
                print 'subworld.left_bound: %s' % str(subworld.left_bound)
                print 'subworld.right_bound: %s' % str(subworld.right_bound)
                print 'subworld.top_bound: %s' % str(subworld.top_bound)
                print 'subworld.bot_bound: %s' % str(subworld.bot_bound)
                print 'row: %s' % str(row)
                print 'col: %s' % str(col)
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

    def _get_new_path(self, src_row, src_col, dst_row, dst_col):
        for subworld in self.world.subworlds:
            subworld.check_bounds(self.world)
        if src_row == dst_row and src_col == dst_col:
            print 'hello2'
            return []
        subworld = self.world.get_current_subworld(src_row, src_col)
        if subworld.is_valid_row_col(dst_row, dst_col):
            # dst_row and dst_col are in current subworld
            return self._get_shortest_path(src_row, src_col, dst_row, dst_col,
                                           subworld)
        # check if src_row and src_col have reached a boundary destination:
        src_tile = Enemy.TilePath(src_row, src_col, None)
        if not subworld.is_valid_row_col(src_row, src_col - 1) and \
                dst_col < src_col and src_col - 1 >= 0 and not \
                isinstance(self.world.grid[src_row][src_col - 1], Wall):
            dst_tile = Enemy.TilePath(src_row, src_col - 1, src_tile)
            return [dst_tile]
        if not subworld.is_valid_row_col(src_row, src_col + 1) and \
                dst_col > src_col and src_col + 1 < World.TOTAL_COLS and not \
                isinstance(self.world.grid[src_row][src_col + 1], Wall):
            dst_tile = Enemy.TilePath(src_row, src_col + 1, src_tile)
            return [dst_tile]
        if not subworld.is_valid_row_col(src_row - 1, src_col) and \
                dst_row < src_row and src_row - 1 >= 0 and not \
                isinstance(self.world.grid[src_row - 1][src_col], Wall):
            dst_tile = Enemy.TilePath(src_row - 1, src_col, src_tile)
            return [dst_tile]
        if not subworld.is_valid_row_col(src_row + 1, src_col) and \
                dst_row > src_row and src_row + 1 < World.TOTAL_ROWS and not \
                isinstance(self.world.grid[src_row + 1][src_col], Wall):
            dst_tile = Enemy.TilePath(src_row + 1, src_col, src_tile)
            return [dst_tile]
        # dst_row and dst_col are not in current subworld and src_row and
        # src_col are not in a boundary destination:
        if dst_col < src_col:
            # dst is left of src
            while subworld.left_bound:
                (curr_dst_row, curr_dst_col) = subworld.left_bound.pop(
                    randint(0, len(subworld.left_bound) - 1))
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    return shortest_path
        if dst_row < src_row:
            # dst is above src
            while subworld.top_bound:
                (curr_dst_row, curr_dst_col) = subworld.top_bound.pop(
                    randint(0, len(subworld.top_bound) - 1))
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    return shortest_path
        if dst_col > src_col:
            # dst is right of src
            while subworld.right_bound:
                (curr_dst_row, curr_dst_col) = subworld.right_bound.pop(
                    randint(0, len(subworld.right_bound) - 1))
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    return shortest_path
        if dst_row > src_row:
            # dst is below src
            while subworld.bot_bound:
                (curr_dst_row, curr_dst_col) = subworld.bot_bound.pop(
                    randint(0, len(subworld.bot_bound) - 1))
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    return shortest_path
        # no path found toward destination.  choose any available path now:
        while subworld.left_bound:
            (curr_dst_row, curr_dst_col) = subworld.left_bound.pop(
                randint(0, len(subworld.left_bound) - 1))
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
            if shortest_path:
                return shortest_path
        while subworld.right_bound:
            (curr_dst_row, curr_dst_col) = subworld.right_bound.pop(
                randint(0, len(subworld.right_bound) - 1))
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
            if shortest_path:
                return shortest_path
        while subworld.top_bound:
            (curr_dst_row, curr_dst_col) = subworld.top_bound.pop(
                randint(0, len(subworld.top_bound) - 1))
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
            if shortest_path:
                return shortest_path
        while subworld.bot_bound:
            (curr_dst_row, curr_dst_col) = subworld.bot_bound.pop(
                randint(0, len(subworld.bot_bound) - 1))
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
            if shortest_path:
                return shortest_path
        print 'hello3'
        return []

    # TODO: limit the breadth-first search depth of _get_shortest_path
    def _get_shortest_path(self, src_row, src_col, dst_row, dst_col, subworld):
        if src_row == dst_row and src_col == dst_col:
            return []
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
                return curr_tile.get_path()
            if curr_tile.row - 1 >= 0 and \
                    subworld.is_valid_row_col(curr_tile.row - 1,
                                              curr_tile.col):
                up_tile = self.world.grid[curr_tile.row - 1][curr_tile.col]
                if not discovered_tiles[curr_tile.row - 1][curr_tile.col]:
                    if (not up_tile) or (up_tile and not \
                            isinstance(up_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row - 1, curr_tile.col,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.row + 1 < World.TOTAL_ROWS and \
                    subworld.is_valid_row_col(curr_tile.row + 1,
                                              curr_tile.col):
                down_tile = self.world.grid[curr_tile.row + 1][curr_tile.col]
                if not discovered_tiles[curr_tile.row + 1][curr_tile.col]:
                    if (not down_tile) or (down_tile and not \
                            isinstance(down_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row + 1, curr_tile.col,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.col - 1 >= 0 and \
                    subworld.is_valid_row_col(curr_tile.row,
                                              curr_tile.col - 1):
                left_tile = self.world.grid[curr_tile.row][curr_tile.col - 1]
                if not discovered_tiles[curr_tile.row][curr_tile.col - 1]:
                    if (not left_tile) or (left_tile and not \
                            isinstance(left_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row, curr_tile.col - 1,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
            if curr_tile.col + 1 < World.TOTAL_COLS and \
                    subworld.is_valid_row_col(curr_tile.row,
                                              curr_tile.col + 1):
                right_tile = self.world.grid[curr_tile.row][curr_tile.col + 1]
                if not discovered_tiles[curr_tile.row][curr_tile.col + 1]:
                    if (not right_tile) or (right_tile and not \
                            isinstance(right_tile, Wall)):
                        tile = Enemy.TilePath(curr_tile.row, curr_tile.col + 1,
                                              curr_tile)
                        undiscovered_tiles.append(tile)
        print 'hmm1'
        return []