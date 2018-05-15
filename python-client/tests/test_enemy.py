import sys
sys.path.append('..')
from world import World
from enemy import Enemy
from stationary_tile import StationaryTile
from moving_tile import MovingTile
from wall import Wall
import unittest

class TestEnemy(unittest.TestCase):

    ''' Testing the do_something() method from enemy.py '''

    def test_food_in_current_subworld(self):
        '''
        Food is in the current subworld as the enemy.
        Verify that enemy.shortest_path[-1] == [(food_row, food_col)] and
        enemy.entering_new_subworld == False.

        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w00f000000000000000w
        w000000000000000000w
        w0000e0000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
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
        food_row = 7
        food_col = 7
        world = World(food_row, food_col)
        enemy = Enemy(world)

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_shortest_path = (food_row, food_col)

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path,
                         (enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col))

    def test_food_in_neighbor_subworld(self):
        '''
        a.  Food is in the left subworld.  Enemy is in the center of the
            subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1]) and
            enemy.entering_new_subworld == False.
        b.  Food is in the right subworld.  Enemy is in the center of the
            subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1]) and
            enemy.entering_new_subworld == False.
        c.  Food is in the top subworld.  Enemy is in the center of the
            subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1]) and
            enemy.entering_new_subworld == False.
        d.  Food is in the bot subworld.  Enemy is in the center of the
            subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1]) and
            enemy.entering_new_subworld == False.
        '''
        # a:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000f00000e00000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 13
        food_col = 7
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_shortest_path = \
            subworld.left_bound[len(subworld.left_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path,
                         (enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col))
        # b:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000e0000fw
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 13
        food_col = 18
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_shortest_path = \
            subworld.right_bound[len(subworld.right_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path,
                         (enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col))
        # c:
        '''
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000f00000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000e00000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 7
        food_col = 13
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_shortest_path = \
            subworld.top_bound[len(subworld.top_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path,
                         (enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col))
        # d:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000e0000fw
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 18
        food_col = 13
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_shortest_path = \
            subworld.bot_bound[len(subworld.bot_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path,
                         (enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col))

    def test_food_in_neighbor_subworld_bound_empty(self):
        '''
        a.  Food is in the left subworld, but the left bound is empty.  Enemy
            is in the center of the subworld.
            Verify that (enemy.shortest_path[-1] ==
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1]) or
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1]) or
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1])
                        ) and enemy.entering_new_subworld == False.
        b.  Food is in the right subworld, but the right bound is empty.  Enemy
            is in the center of the subworld.
            Verify that (enemy.shortest_path[-1] ==
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1]) or
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1]) or
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1])
                        ) and enemy.entering_new_subworld == False.
        c.  Food is in the top subworld, but the top bound is empty.  Enemy is
            in the center of the subworld.
            Verify that (enemy.shortest_path[-1] ==
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1]) or
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1]) or
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1])
                        ) and enemy.entering_new_subworld == False.
        d.  Food is in the bot subworld, but the bot bound is empty.  Enemy is
            in the center of the subworld.
            Verify that (enemy.shortest_path[-1] ==
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1]) or
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1]) or
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1])
                        ) and enemy.entering_new_subworld == False.
        '''
        # a:
        '''
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
        w000000000w00000000w
        w000000000w00000000w
        w000000000w00000000w
        w000000f00w00e00000w
        w000000000w00000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 13
        food_col = 7
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        # add walls in the left bound
        for row in range(10, 14 + 1):
            world.grid[row][10] = Wall(row, 10)
        subworld.check_bounds(world)

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_right_shortest_path = \
            subworld.right_bound[len(subworld.right_bound) / 2]
        new_last_top_shortest_path = \
            subworld.top_bound[len(subworld.top_bound) / 2]
        new_last_bot_shortest_path = \
            subworld.bot_bound[len(subworld.bot_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertIn((enemy.shortest_path[-1].row,
                       enemy.shortest_path[-1].col),
                       [new_last_right_shortest_path,
                         new_last_bot_shortest_path,
                         new_last_top_shortest_path])
        # b:
        '''
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
        w0000000000000w0000w
        w0000000000000w0000w
        w0000000000000w0000w
        w000000000000ew000fw
        w0000000000000w0000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 13
        food_col = 18
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        # add walls in the right bound
        for row in range(10, 14 + 1):
            world.grid[row][14] = Wall(row, 14)
        subworld.check_bounds(world)

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_left_shortest_path = \
            subworld.left_bound[len(subworld.left_bound) / 2]
        new_last_top_shortest_path = \
            subworld.top_bound[len(subworld.top_bound) / 2]
        new_last_bot_shortest_path = \
            subworld.bot_bound[len(subworld.bot_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertIn((enemy.shortest_path[-1].row,
                       enemy.shortest_path[-1].col),
                       [new_last_top_shortest_path,
                         new_last_bot_shortest_path,
                         new_last_left_shortest_path])
        # c:
        '''
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000f00000w
        w000000000000000000w
        w000000000000000000w
        w000000000wwwww0000w
        w000000000000000000w
        w000000000000000000w
        w000000000000e00000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 7
        food_col = 13
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        # add walls in the top bound
        for col in range(10, 14 + 1):
            world.grid[10][col] = Wall(10, col)
        subworld.check_bounds(world)

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_right_shortest_path = \
            subworld.right_bound[len(subworld.right_bound) / 2]
        new_last_left_shortest_path = \
            subworld.left_bound[len(subworld.left_bound) / 2]
        new_last_bot_shortest_path = \
            subworld.bot_bound[len(subworld.bot_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertIn((enemy.shortest_path[-1].row,
                       enemy.shortest_path[-1].col),
                       [new_last_right_shortest_path,
                         new_last_bot_shortest_path,
                         new_last_left_shortest_path])
        # d:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000e0000fw
        w000000000wwwww0000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 18
        food_col = 13
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at row 13 and col 13
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 13)
        subworld = world.get_current_subworld(13, 13)
        enemy.shortest_path = []
        # add walls in the bot bound
        for col in range(10, 14 + 1):
            world.grid[14][col] = Wall(14, col)
        subworld.check_bounds(world)

        new_entering_new_subworld = enemy.entering_new_subworld
        new_last_right_shortest_path = \
            subworld.right_bound[len(subworld.right_bound) / 2]
        new_last_left_shortest_path = \
            subworld.left_bound[len(subworld.left_bound) / 2]
        new_last_top_shortest_path = \
            subworld.top_bound[len(subworld.top_bound) / 2]

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertIn((enemy.shortest_path[-1].row,
                       enemy.shortest_path[-1].col),
                       [new_last_right_shortest_path,
                         new_last_top_shortest_path,
                         new_last_left_shortest_path])

    def test_enter_bound_popped(self):
        '''
        a.  Enemy is about to enter the left bound and then go to left subworld
            to get the food.
            Verify that the former
            (subworld.left_bound[len(subworld.left_bound) / 2][0],
             subworld.left_bound[len(subworld.left_bound) / 2][1]) is not in
            subworld.left_bound anymore and
            enemy.entering_new_subworld == True.
        b.  Enemy is about to enter the right bound and then go to right
            subworld to get the food.
            Verify that the former
            (subworld.right_bound[len(subworld.right_bound) / 2][0],
             subworld.right_bound[len(subworld.right_bound) / 2][1]) is not in
            subworld.right_bound anymore and
            enemy.entering_new_subworld == True.
        c.  Enemy is about to enter the top bound and then go to top subworld
            to get the food.
            Verify that the former
            (subworld.top_bound[len(subworld.top_bound) / 2][0],
             subworld.top_bound[len(subworld.top_bound) / 2][1]) is not in
            subworld.top_bound anymore and
            enemy.entering_new_subworld == True.
        d.  Enemy is about to enter the bot bound and then go to bot subworld
            to get the food.
            Verify that the former
            (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
             subworld.bot_bound[len(subworld.bot_bound) / 2][1]) is not in
            subworld.bot_bound anymore and
            enemy.entering_new_subworld == True.
        '''
        # a:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w0000000f00e0000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 12
        food_col = 8
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at (12, 11) before entering left bound (12, 10) in SW10
        subworld = world.get_current_subworld(12, 11)
        former_left_bound = subworld.left_bound[len(subworld.left_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 11,
                          StationaryTile.DIMS[0] * 12)
        enemy.shortest_path = []

        new_entering_new_subworld = True
        new_last_shortest_path = [(Enemy.TilePath(12, 9,
                                                 Enemy.TilePath(12, 10, None)))]

        enemy.do_something()
        # keep on moving until enemy reaches former_left_bound
        while enemy.position[0] != \
                (former_left_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_left_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (12, 10).  shortest_path is now empty.
        enemy.do_something()
        # enter the new subworld
        enemy.do_something()

        self.assertNotIn(former_left_bound, subworld.left_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(len(new_last_shortest_path), len(enemy.shortest_path))
        for i in range(len(new_last_shortest_path)):
            self.assertEqual(new_last_shortest_path[i].row,
                             enemy.shortest_path[i].row)
            self.assertEqual(new_last_shortest_path[i].col,
                             enemy.shortest_path[i].col)
            self.assertEqual(new_last_shortest_path[i].parent.row,
                             enemy.shortest_path[i].parent.row)
            self.assertEqual(new_last_shortest_path[i].parent.col,
                             enemy.shortest_path[i].parent.col)
            # parents should be None
            self.assertEqual(new_last_shortest_path[i].parent.parent,
                             enemy.shortest_path[i].parent.parent)
        # b:
        '''
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
        w000000000000000000w
        w000000000000000000w
        w000000000000e00f00w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 12
        food_col = 16
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at (12, 13) before entering right bound (12, 14) in SW10
        subworld = world.get_current_subworld(12, 13)
        former_right_bound = subworld.right_bound[len(subworld.right_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 13,
                          StationaryTile.DIMS[0] * 12)
        enemy.shortest_path = []

        new_entering_new_subworld = True
        new_last_shortest_path = [(Enemy.TilePath(12, 15,
                                                 Enemy.TilePath(12, 14, None)))]

        enemy.do_something()
        # keep on moving until enemy reaches former_right_bound
        while enemy.position[0] != \
                (former_right_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_right_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (12, 14).  shortest_path is now empty.
        enemy.do_something()
        # enter the new subworld
        enemy.do_something()

        self.assertNotIn(former_right_bound, subworld.right_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(len(new_last_shortest_path), len(enemy.shortest_path))
        for i in range(len(new_last_shortest_path)):
            self.assertEqual(new_last_shortest_path[i].row,
                             enemy.shortest_path[i].row)
            self.assertEqual(new_last_shortest_path[i].col,
                             enemy.shortest_path[i].col)
            self.assertEqual(new_last_shortest_path[i].parent.row,
                             enemy.shortest_path[i].parent.row)
            self.assertEqual(new_last_shortest_path[i].parent.col,
                             enemy.shortest_path[i].parent.col)
            # parents should be None
            self.assertEqual(new_last_shortest_path[i].parent.parent,
                             enemy.shortest_path[i].parent.parent)
        # c:
        '''
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w00000000000f000000w
        w000000000000000000w
        w000000000000000000w
        w00000000000e000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
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
        food_row = 3
        food_col = 12
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at (6, 12) before entering top bound (5, 12) in SW6
        subworld = world.get_current_subworld(6, 12)
        former_top_bound = subworld.top_bound[len(subworld.top_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 12,
                          StationaryTile.DIMS[0] * 6)
        enemy.shortest_path = []

        new_entering_new_subworld = True
        new_last_shortest_path = [(Enemy.TilePath(4, 12,
                                                 Enemy.TilePath(5, 12, None)))]

        enemy.do_something()
        # keep on moving until enemy reaches former_top_bound
        while enemy.position[0] != \
                (former_top_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_top_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (5, 12).  shortest_path is now empty.
        enemy.do_something()
        # enter the new subworld
        enemy.do_something()

        self.assertNotIn(former_top_bound, subworld.top_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(len(new_last_shortest_path), len(enemy.shortest_path))
        for i in range(len(new_last_shortest_path)):
            self.assertEqual(new_last_shortest_path[i].row,
                             enemy.shortest_path[i].row)
            self.assertEqual(new_last_shortest_path[i].col,
                             enemy.shortest_path[i].col)
            self.assertEqual(new_last_shortest_path[i].parent.row,
                             enemy.shortest_path[i].parent.row)
            self.assertEqual(new_last_shortest_path[i].parent.col,
                             enemy.shortest_path[i].parent.col)
            # parents should be None
            self.assertEqual(new_last_shortest_path[i].parent.parent,
                             enemy.shortest_path[i].parent.parent)
        # d:
        '''
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w00000000000e000000w
        w000000000000000000w
        w000000000000000000w
        w00000000000f000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 11
        food_col = 12
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at (8, 12) before entering bot bound (9, 12) in SW6
        subworld = world.get_current_subworld(8, 12)
        former_bot_bound = subworld.bot_bound[len(subworld.bot_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 12,
                          StationaryTile.DIMS[0] * 8)
        enemy.shortest_path = []

        new_entering_new_subworld = True
        new_last_shortest_path = [(Enemy.TilePath(10, 12,
                                                 Enemy.TilePath(9, 12, None)))]

        enemy.do_something()
        # keep on moving until enemy reaches former_bot_bound
        while enemy.position[0] != \
                (former_bot_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_bot_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (9, 12).  shortest_path is now empty.
        enemy.do_something()
        # enter the new subworld
        enemy.do_something()

        self.assertNotIn(former_bot_bound, subworld.bot_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(len(new_last_shortest_path), len(enemy.shortest_path))
        for i in range(len(new_last_shortest_path)):
            self.assertEqual(new_last_shortest_path[i].row,
                             enemy.shortest_path[i].row)
            self.assertEqual(new_last_shortest_path[i].col,
                             enemy.shortest_path[i].col)
            self.assertEqual(new_last_shortest_path[i].parent.row,
                             enemy.shortest_path[i].parent.row)
            self.assertEqual(new_last_shortest_path[i].parent.col,
                             enemy.shortest_path[i].parent.col)
            # parents should be None
            self.assertEqual(new_last_shortest_path[i].parent.parent,
                             enemy.shortest_path[i].parent.parent)

    def test_in_bound_enter_alternate_bound(self):
        '''
        Enemy is going to a left bound and food is in the bottom-left
        direction, but bound is blocked.
        Verify that the former
        (subworld.left_bound[len(subworld.left_bound) / 2][0],
            subworld.left_bound[len(subworld.left_bound) / 2][1]) is not in
        subworld.left_bound anymore and then the next
        (subworld.left_bound[len(subworld.left_bound) / 2][0],
            subworld.left_bound[len(subworld.left_bound) / 2][1]) becomes the new
        destination.
        enemy.entering_new_subworld == False.
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
        w000000000000000000w
        w000000000000000000w
        w000w0e000000000000w
        w00f000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 13
        food_col = 3
        world = World(food_row, food_col)
        world.grid[12][4] = Wall(12, 4)
        enemy = Enemy(world)
        # enemy start at (12, 6) before entering left bound (12, 5) in SW9
        subworld = world.get_current_subworld(12, 6)
        former_left_bound = subworld.left_bound[len(subworld.left_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 6,
                          StationaryTile.DIMS[0] * 12)
        enemy.shortest_path = []

        new_entering_new_subworld = False

        enemy.do_something()
        # keep on moving until enemy reaches former_left_bound
        while enemy.position[0] != \
                (former_left_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_left_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (12, 5).  shortest_path is now empty.
        enemy.do_something()
        # entrance to left subworld is blocked by a Wall at (12, 4).  The last
        # shortest path destination is the next left bound.
        enemy.do_something()
        new_last_shortest_path = \
            (subworld.left_bound[len(subworld.left_bound) / 2][0],
             subworld.left_bound[len(subworld.left_bound) / 2][1])

        self.assertNotIn(former_left_bound, subworld.left_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path, (enemy.shortest_path[-1].row,
                                                  enemy.shortest_path[-1].col))

    def test_enemy_in_bound_food_not_in_dir_other_bounds_empty(self):
        '''
        Enemy is about to enter the top bound and food is not in that
        direction, but the other bounds are empty.
        Verify that the enemy still goes in that direction:
        Verify that the former
            (subworld.top_bound[len(subworld.top_bound) / 2][0],
             subworld.top_bound[len(subworld.top_bound) / 2][1]) is not in
            subworld.top_bound anymore and
            enemy.entering_new_subworld == True.
        Map:
        wwwwwwwwwwwwwwwwwwww
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000e00000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w0000000000000f0000w
        w000000000000000000w
        w000000000000000000w
        wwwwwwwwwwwwwwwwwwww
        '''
        food_row = 16
        food_col = 14
        world = World(food_row, food_col)
        enemy = Enemy(world)
        # enemy start at (6, 7) before entering top bound (5, 7) in SW5
        subworld = world.get_current_subworld(6, 7)
        former_top_bound = subworld.top_bound[len(subworld.top_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 6,
                          StationaryTile.DIMS[0] * 7)
        enemy.shortest_path = []
        subworld.bot_bound = []
        subworld.left_bound = []
        subworld.right_bound = []

        new_entering_new_subworld = True
        new_last_shortest_path = [(Enemy.TilePath(4, 7,
                                                 Enemy.TilePath(5, 7, None)))]

        enemy.do_something()
        # keep on moving until enemy reaches former_top_bound
        while enemy.position[0] != \
                (former_top_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_top_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (5, 7).  shortest_path is now empty.
        enemy.do_something()
        # enter the new subworld
        enemy.do_something()

        self.assertNotIn(former_top_bound, subworld.top_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(len(new_last_shortest_path), len(enemy.shortest_path))
        for i in range(len(new_last_shortest_path)):
            self.assertEqual(new_last_shortest_path[i].row,
                             enemy.shortest_path[i].row)
            self.assertEqual(new_last_shortest_path[i].col,
                             enemy.shortest_path[i].col)
            self.assertEqual(new_last_shortest_path[i].parent.row,
                             enemy.shortest_path[i].parent.row)
            self.assertEqual(new_last_shortest_path[i].parent.col,
                             enemy.shortest_path[i].parent.col)
            # parents should be None
            self.assertEqual(new_last_shortest_path[i].parent.parent,
                             enemy.shortest_path[i].parent.parent)

    def test_enemy_in_bound_other_bounds_empty_food_not_in_dir_bound_blocked(self):
        '''
        Enemy is about to enter the bot bound, but the bound is blocked, the
        food is not in that direction, and other bounds are empty.
        Verify that the enemy chooses the next bot bound:
        (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
            subworld.bot_bound[len(subworld.bot_bound) / 2][1]) is not in
        subworld.bot_bound anymore and then the next
        (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
            subworld.bot_bound[len(subworld.bot_bound) / 2][1]) becomes the new
        destination.
        enemy.entering_new_subworld == False.
        Map:
        wwwwwwwwwwwwwwwwwwww
        wf00000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000e00000000000w
        w000000000000000000w
        w000000w00000000000w
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
        food_row = 1
        food_col = 1
        world = World(food_row, food_col)
        world.grid[10][7] = Wall(10, 7)
        enemy = Enemy(world)
        # enemy start at (8, 7) before entering bot bound (9, 7) in SW5
        subworld = world.get_current_subworld(8, 7)
        former_bot_bound = subworld.left_bound[len(subworld.bot_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 8,
                          StationaryTile.DIMS[0] * 7)
        enemy.shortest_path = []
        subworld.left_bound = []
        subworld.top_bound = []
        subworld.right_bound = []

        new_entering_new_subworld = False

        enemy.do_something()
        # keep on moving until enemy reaches former_bot_bound
        while enemy.position[0] != \
                (former_bot_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_bot_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (9, 7).  shortest_path is now empty.
        enemy.do_something()
        # entrance to bot subworld is blocked by a Wall at (10, 7).  The last
        # shortest path destination is the next bot bound.
        enemy.do_something()
        new_last_shortest_path = \
            (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
             subworld.bot_bound[len(subworld.bot_bound) / 2][1])

        self.assertNotIn(former_bot_bound, subworld.bot_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path, (enemy.shortest_path[-1].row,
                                                  enemy.shortest_path[-1].col))

    def test_no_path(self):
        # TODO: 
        '''
        Enemy is about to enter the right bound, the bound is blocked, all
        other bounds are empty, and there are no more tiles available in the
        right bound.
        Verify that shortest_path == [].
        Map:
        wwwwwwwwwwwwwwwwwwww
        wf00000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000000000000000w
        w000000e00000000000w
        w000000000000000000w
        w000000w00000000000w
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
        food_row = 1
        food_col = 1
        world = World(food_row, food_col)
        world.grid[10][7] = Wall(10, 7)
        enemy = Enemy(world)
        # enemy start at (8, 7) before entering bot bound (9, 7) in SW5
        subworld = world.get_current_subworld(8, 7)
        former_bot_bound = subworld.left_bound[len(subworld.bot_bound) / 2]
        enemy.position = (StationaryTile.DIMS[1] * 8,
                          StationaryTile.DIMS[0] * 7)
        enemy.shortest_path = []
        subworld.left_bound = []
        subworld.top_bound = []
        subworld.right_bound = []

        new_entering_new_subworld = False

        enemy.do_something()
        # keep on moving until enemy reaches former_bot_bound
        while enemy.position[0] != \
                (former_bot_bound[1] * StationaryTile.DIMS[0]) or \
                enemy.position[1] != \
                (former_bot_bound[0] * StationaryTile.DIMS[1]):
            enemy.do_something()
        # pop the shortest path to (9, 7).  shortest_path is now empty.
        enemy.do_something()
        # entrance to bot subworld is blocked by a Wall at (10, 7).  The last
        # shortest path destination is the next bot bound.
        enemy.do_something()
        new_last_shortest_path = \
            (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
             subworld.bot_bound[len(subworld.bot_bound) / 2][1])

        self.assertNotIn(former_bot_bound, subworld.bot_bound)
        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual(new_last_shortest_path, (enemy.shortest_path[-1].row,
                                                  enemy.shortest_path[-1].col))
        

if __name__ == '__main__':
    unittest.main()