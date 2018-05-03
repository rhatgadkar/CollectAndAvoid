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
        self.entering_new_subworld = False
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
                # no shortest path found for new destination
                print 'frozen'
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
            return []
        subworld = self.world.get_current_subworld(src_row, src_col)
        if subworld.is_valid_row_col(dst_row, dst_col):
            # dst_row and dst_col are in current subworld
            shortest_path = self._get_shortest_path(src_row, src_col, dst_row,
                                                    dst_col, subworld)
            if shortest_path:
                print 'path in bound'
                return shortest_path
        # check if src_row and src_col have reached a boundary destination:
        src_tile = Enemy.TilePath(src_row, src_col, None)
        dst_tile = None
        neighbor_subworld = self.world.get_current_subworld(src_row,
                                                            src_col - 1)
        if not subworld.is_valid_row_col(src_row, src_col - 1) and not \
                isinstance(self.world.grid[src_row][src_col - 1], Wall) and \
                (not neighbor_subworld.all_bounds_empty() or \
                neighbor_subworld.is_valid_row_col(dst_row, dst_col)) and \
                (src_row, src_col) in subworld.left_bound and not \
                self.entering_new_subworld:
            dst_tile = Enemy.TilePath(src_row, src_col - 1, src_tile)
            if dst_col < src_col:
                self.entering_new_subworld = True
                subworld.left_bound.pop(len(subworld.left_bound) / 2)
                print 'reach left'
                return [dst_tile]
        neighbor_subworld = self.world.get_current_subworld(src_row,
                                                            src_col + 1)
        if not subworld.is_valid_row_col(src_row, src_col + 1) and not \
                isinstance(self.world.grid[src_row][src_col + 1], Wall) and \
                (not neighbor_subworld.all_bounds_empty() or \
                neighbor_subworld.is_valid_row_col(dst_row, dst_col)) and \
                (src_row, src_col) in subworld.right_bound and not \
                self.entering_new_subworld:
            dst_tile = Enemy.TilePath(src_row, src_col + 1, src_tile)
            if dst_col > src_col:
                self.entering_new_subworld = True
                subworld.right_bound.pop(len(subworld.right_bound) / 2)
                print 'reach right'
                return [dst_tile]
        neighbor_subworld = self.world.get_current_subworld(src_row - 1,
                                                            src_col)
        if not subworld.is_valid_row_col(src_row - 1, src_col) and not \
                isinstance(self.world.grid[src_row - 1][src_col], Wall) and \
                (not neighbor_subworld.all_bounds_empty() or \
                neighbor_subworld.is_valid_row_col(dst_row, dst_col)) and \
                (src_row, src_col) in subworld.top_bound and not \
                self.entering_new_subworld:
            dst_tile = Enemy.TilePath(src_row - 1, src_col, src_tile)
            if dst_row < src_row:
                self.entering_new_subworld = True
                subworld.top_bound.pop(len(subworld.top_bound) / 2)
                print 'reach top'
                return [dst_tile]
        neighbor_subworld = self.world.get_current_subworld(src_row + 1,
                                                            src_col)
        if not subworld.is_valid_row_col(src_row + 1, src_col) and not \
                isinstance(self.world.grid[src_row + 1][src_col], Wall) and \
                (not neighbor_subworld.all_bounds_empty() or \
                neighbor_subworld.is_valid_row_col(dst_row, dst_col)) and \
                (src_row, src_col) in subworld.bot_bound and not \
                self.entering_new_subworld:
            dst_tile = Enemy.TilePath(src_row + 1, src_col, src_tile)
            if dst_row > src_row:
                self.entering_new_subworld = True
                subworld.bot_bound.pop(len(subworld.bot_bound) / 2)
                print 'reach bot'
                return [dst_tile]
        # food is not in the new subworld's direction, and pop the visited tile
        # from the bound:
        if not self.entering_new_subworld:
            if (src_row, src_col) in subworld.left_bound:
                subworld.left_bound.pop(len(subworld.left_bound) / 2)
            elif (src_row, src_col) in subworld.right_bound:
                subworld.right_bound.pop(len(subworld.right_bound) / 2)
            elif (src_row, src_col) in subworld.top_bound:
                subworld.top_bound.pop(len(subworld.top_bound) / 2)
            elif (src_row, src_col) in subworld.bot_bound:
                subworld.bot_bound.pop(len(subworld.bot_bound) / 2)
        # dst_row and dst_col are not in current subworld and src_row and
        # src_col are not in a boundary destination toward the food:
        if dst_col < src_col:
            while subworld.left_bound:
                (curr_dst_row, curr_dst_col) = subworld.left_bound[
                    len(subworld.left_bound) / 2]
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    self.entering_new_subworld = False
                    print 'go to left'
                    return shortest_path
                subworld.left_bound.pop(len(subworld.left_bound) / 2)
        if dst_row < src_row:
            while subworld.top_bound:
                (curr_dst_row, curr_dst_col) = subworld.top_bound[
                    len(subworld.top_bound) / 2]
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    self.entering_new_subworld = False
                    print 'go to top'
                    return shortest_path
                subworld.top_bound.pop(len(subworld.top_bound) / 2)
        if dst_col > src_col:
            while subworld.right_bound:
                (curr_dst_row, curr_dst_col) = subworld.right_bound[
                    len(subworld.right_bound) / 2]
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    self.entering_new_subworld = False
                    print 'go to right'
                    return shortest_path
                subworld.right_bound.pop(len(subworld.right_bound) / 2)
        if dst_row > src_row:
            while subworld.bot_bound:
                (curr_dst_row, curr_dst_col) = subworld.bot_bound[
                    len(subworld.bot_bound) / 2]
                shortest_path = self._get_shortest_path(src_row, src_col,
                                                        curr_dst_row,
                                                        curr_dst_col, subworld)
                if shortest_path:
                    self.entering_new_subworld = False
                    print 'go to bot'
                    return shortest_path
                subworld.bot_bound.pop(len(subworld.bot_bound) / 2)
        # at boundary destination, but destination is not in direction.
        # no path toward destination, so go anyway in this direction.
        if dst_tile:
            self.entering_new_subworld = True
            return [dst_tile]
        # no path found toward destination.  choose any available path now.
        while subworld.left_bound:
            (curr_dst_row, curr_dst_col) = subworld.left_bound[
                len(subworld.left_bound) / 2]
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                    curr_dst_row,
                                                    curr_dst_col, subworld)
            if shortest_path:
                self.entering_new_subworld = False
                print 'no path. go to left bound'
                return shortest_path
            subworld.left_bound.pop(len(subworld.left_bound) / 2)
        while subworld.right_bound:
            (curr_dst_row, curr_dst_col) = subworld.right_bound[
                len(subworld.right_bound) / 2]
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                    curr_dst_row,
                                                    curr_dst_col, subworld)
            if shortest_path:
                self.entering_new_subworld = False
                print 'no path. go to right bound'
                return shortest_path
            subworld.right_bound.pop(len(subworld.right_bound) / 2)
        while subworld.top_bound:
            (curr_dst_row, curr_dst_col) = subworld.top_bound[
                len(subworld.top_bound) / 2]
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                    curr_dst_row,
                                                    curr_dst_col, subworld)
            if shortest_path:
                self.entering_new_subworld = False
                print 'no path. go to top bound'
                return shortest_path
            subworld.top_bound.pop(len(subworld.top_bound) / 2)
        while subworld.bot_bound:
            (curr_dst_row, curr_dst_col) = subworld.bot_bound[
                len(subworld.bot_bound) / 2]
            shortest_path = self._get_shortest_path(src_row, src_col,
                                                    curr_dst_row,
                                                    curr_dst_col, subworld)
            if shortest_path:
                self.entering_new_subworld = False
                print 'no path. go to bot bound'
                return shortest_path
            subworld.bot_bound.pop(len(subworld.bot_bound) / 2)
        return []

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
        return []