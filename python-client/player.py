from keys import Keys
from stationary_tile import StationaryTile
from moving_tile import MovingTile
from world import World
from wall import Wall
from food import Food

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
        x, y = self.position
        if Keys.up:
            y -= MovingTile.VERT_SPEED
        if Keys.down:
            y += MovingTile.VERT_SPEED
        if Keys.left:
            x -= MovingTile.HORIZ_SPEED
        if Keys.right:
            x += MovingTile.HORIZ_SPEED
        self.position = (x, y)
        collided_tile = MovingTile.check_collision(self)
        if collided_tile:
            if isinstance(collided_tile, Wall):
                self.dead = True
            elif isinstance(collided_tile, Food) and not self.got_food:
                self.score += 1
                self.got_food = True
                self.world.grid[collided_tile.row][collided_tile.col] = None
                self.add_new_wall()
                self.add_new_food()
        else:
            self.got_food = False