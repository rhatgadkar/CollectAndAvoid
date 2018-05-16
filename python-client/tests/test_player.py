import sys
sys.path.append('..')
from world import World
from player import Player
from stationary_tile import StationaryTile
from moving_tile import MovingTile
from wall import Wall
from enemy import Enemy
from keys import Keys
import unittest

class TestPlayer(unittest.TestCase):

    ''' Testing the do_something() method from player.py '''

    def test_no_action(self):
        '''
        Player does not collide with any object and moves from default Keys.up.
        Verify that player variables are unchanged except y position.

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
        w000000000f00000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w0000p0000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        Keys.reset()
        food_row = 10
        food_col = 10
        world = World(food_row, food_col)
        player = Player(world)

        new_x = player.position[0]
        new_y = player.position[1] - MovingTile.VERT_SPEED
        new_dead = player.dead
        new_got_food = player.got_food
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_collide_from_bot(self):
        '''
        Player collides with food from bottom, by moving up.
        Verify that player's got_food changes to True, y position changes, and
        score increments.

        Map before collision:
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
        w000000000f00000000w
        w000000000p00000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        Keys.reset()
        food_row = 10
        food_col = 10
        world = World(food_row, food_col)
        player = Player(world)
        player_row = 11
        player_col = 10
        player_y = StationaryTile.DIMS[1] * player_row
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)

        new_x = player.position[0]
        new_y = player.position[1] - MovingTile.VERT_SPEED
        new_dead = player.dead
        new_got_food = True
        new_score = player.score + 1

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_collide_from_right(self):
        '''
        Player collides with wall from right, by moving left.
        Verify that player's dead changes to True and x position changes.

        Map before collision:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000f00000000w
        w000000000000000000w
        w000000000wp0000000w
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
        Keys.reset()
        food_row = 8
        food_col = 10
        world = World(food_row, food_col)
        world.grid[10][10] = Wall(10, 10)
        player = Player(world)
        player_row = 10
        player_col = 11
        player_y = StationaryTile.DIMS[1] * player_row
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)
        Keys.set_left()

        new_x = player.position[0] - MovingTile.HORIZ_SPEED
        new_y = player.position[1]
        new_dead = True
        new_got_food = player.got_food
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_collide_from_top(self):
        '''
        Player collides with wall from top, by moving down.
        Verify that player's dead changes to True and y position changes.

        Map before collision:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000f00000000w
        w000000000p00000000w
        w000000000w00000000w
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
        Keys.reset()
        food_row = 8
        food_col = 10
        world = World(food_row, food_col)
        world.grid[10][10] = Wall(10, 10)
        player = Player(world)
        player_row = 9
        player_col = 10
        player_y = StationaryTile.DIMS[1] * (player_row + 1) - \
                MovingTile.DIMS[1]
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)
        Keys.set_down()

        new_x = player.position[0]
        new_y = player.position[1] + MovingTile.VERT_SPEED
        new_dead = True
        new_got_food = player.got_food
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_collide_from_left(self):
        '''
        Player collides with food from left, by moving right.
        Verify that player's got_food changes to True, x position changes, and
        score increments.

        Map before collision:
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
        w00000000pf00000000w
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
        Keys.reset()
        food_row = 10
        food_col = 10
        world = World(food_row, food_col)
        player = Player(world)
        player_row = 10
        player_col = 9
        player_y = StationaryTile.DIMS[1] * player_row
        player_x = StationaryTile.DIMS[0] * (player_col + 1) - \
                MovingTile.DIMS[0]
        player.position = (player_x, player_y)
        Keys.set_right()

        new_x = player.position[0] + MovingTile.HORIZ_SPEED
        new_y = player.position[1]
        new_dead = player.dead
        new_got_food = True
        new_score = player.score + 1

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_during_food_collision(self):
        '''
        Verify score does not increment during collision when got_food is
        already True.  Verify that player's got_food remains True, y position
        changes, and score remains the same.
        '''
        Keys.reset()
        food_row = 10
        food_col = 10
        world = World(food_row, food_col)
        player = Player(world)
        player_row = 10
        player_col = 10
        player_y = StationaryTile.DIMS[1] * player_row
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)
        player.got_food = True

        new_x = player.position[0]
        new_y = player.position[1] - MovingTile.VERT_SPEED
        new_dead = player.dead
        new_got_food = player.got_food
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_after_food_collision(self):
        '''
        Verify that got_food is set to False after a food collision is done and
        player is in a tile space that does not contain anything.
        Verify that the y position changes and score remains the same.
        '''
        Keys.reset()
        food_row = 10
        food_col = 10
        world = World(food_row, food_col)
        player = Player(world)
        player_row = 9
        player_col = 10
        player_y = StationaryTile.DIMS[1] * player_row
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)
        player.got_food = True

        new_x = player.position[0]
        new_y = player.position[1] - MovingTile.VERT_SPEED
        new_dead = player.dead
        new_got_food = False
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

    def test_collide_enemy_from_top(self):
        '''
        Player collides with enemy from top, by moving down.
        Verify that player's dead changes to True and y position changes.

        Map before collision:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000f00000000w
        w000000000p00000000w
        w000000000e00000000w
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
        Keys.reset()
        food_row = 8
        food_col = 10
        world = World(food_row, food_col)
        enemy_row = 10
        enemy_col = 10
        enemy = Enemy(world)
        enemy.position = (StationaryTile.DIMS[1] * enemy_row,
                          StationaryTile.DIMS[0] * enemy_col)
        player = Player(world)
        player_row = 9
        player_col = 10
        player_y = StationaryTile.DIMS[1] * (player_row + 1) - \
                MovingTile.DIMS[1]
        player_x = StationaryTile.DIMS[0] * player_col
        player.position = (player_x, player_y)
        Keys.set_down()

        new_x = player.position[0]
        new_y = player.position[1] + MovingTile.VERT_SPEED
        new_dead = True
        new_got_food = player.got_food
        new_score = player.score

        player.do_something()

        self.assertEqual(new_x, player.position[0])
        self.assertEqual(new_y, player.position[1])
        self.assertEqual(new_dead, player.dead)
        self.assertEqual(new_got_food, player.got_food)
        self.assertEqual(new_score, player.score)

if __name__ == '__main__':
    unittest.main()