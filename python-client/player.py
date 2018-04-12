from keys import Keys
from stationary_tile import StationaryTile
from moving_tile import MovingTile
from world import World
from wall import Wall
from food import Food
from random import randint

class Player(MovingTile):
    STARTING_COL = 5
    STARTING_ROW = 15
    STARTING_X = STARTING_COL * StationaryTile.DIMS[0]
    STARTING_Y = STARTING_ROW * StationaryTile.DIMS[1]

    def __init__(self, world):
        super(self.__class__, self).__init__(world)
        self.position = (Player.STARTING_X, Player.STARTING_Y)
        self.color = (0, 255, 0)
        self.dead = False
        self.score = 0

    def do_something(self):
        #import pdb; pdb.set_trace()
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
        collided_tile = MovingTile._check_collision(self)
        if collided_tile:
            if isinstance(collided_tile, Wall):
                self.dead = True
            elif isinstance(collided_tile, Food) and not self.got_food:
                self.score += 1
                self.got_food = True
                self.world.grid[collided_tile.row][collided_tile.col] = None
                # add new wall tile in location not continaining any tile
                while True:
                    new_wall_row = randint(0, World.BOT_ROW)
                    new_wall_col = randint(0, World.RIGHT_COL)
                    new_wall = Wall(new_wall_row, new_wall_col)
                    if self.world.grid[new_wall_row][new_wall_col] != None:
                        continue
                    if MovingTile._bounding_box(self, new_wall):
                        continue
                    self.world.grid[new_wall_row][new_wall_col] = new_wall
                    break
                # add new food tile in location not continaining any tile
                while True:
                    new_food_row = randint(0, World.BOT_ROW)
                    new_food_col = randint(0, World.RIGHT_COL)
                    new_food = Food(new_food_row, new_food_col)
                    if self.world.grid[new_food_row][new_food_col] != None:
                        continue
                    if self._bounding_box(new_food):
                        continue
                    self.world.grid[new_food_row][new_food_col] = new_food
                    break
        else:
            self.got_food = False