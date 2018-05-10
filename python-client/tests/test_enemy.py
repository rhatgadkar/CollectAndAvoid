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

    def test_enemy_in_bound_food_neighbor(self):
        '''
        a.  Enemy is in the left bound, and food is in the left subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1] - 1),
                enemy.entering_new_subworld == True, and
                (subworld.left_bound[len(subworld.left_bound) / 2][0],
                 subworld.left_bound[len(subworld.left_bound) / 2][1])
                not in subworld.left_bound.
        b.  Enemy is in the right bound, and food is in the right subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1] + 1),
                enemy.entering_new_subworld == True, and
                (subworld.right_bound[len(subworld.right_bound) / 2][0],
                 subworld.right_bound[len(subworld.right_bound) / 2][1])
                not in subworld.right_bound.
        c.  Enemy is in the top bound, and food is in the top subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1] + 1),
                enemy.entering_new_subworld == True, and
                (subworld.top_bound[len(subworld.top_bound) / 2][0],
                 subworld.top_bound[len(subworld.top_bound) / 2][1])
                not in subworld.top_bound.
        d.  Enemy is in the bot bound, and food is in the bot subworld.
            Verify that enemy.shortest_path[-1] ==
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1] + 1),
                enemy.entering_new_subworld == True, and
                (subworld.bot_bound[len(subworld.bot_bound) / 2][0],
                 subworld.bot_bound[len(subworld.bot_bound) / 2][1])
                not in subworld.bot_bound.
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
        w000000000e00000000w
        w000000f00000000000w
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
        # enemy start at row 12 and col 10
        enemy.position = (StationaryTile.DIMS[1] * 12,
                          StationaryTile.DIMS[0] * 10)
        subworld = world.get_current_subworld(12, 10)
        enemy.shortest_path = []
        left_bound = subworld.left_bound[len(subworld.left_bound) / 2]

        new_entering_new_subworld = True
        new_last_shortest_path = (left_bound[0], left_bound[1] - 1)

        enemy.do_something()

        self.assertEqual(new_entering_new_subworld,
                         enemy.entering_new_subworld)
        self.assertEqual((enemy.shortest_path[-1].row,
                          enemy.shortest_path[-1].col), new_last_shortest_path)
        self.assertNotIn(left_bound, subworld.left_bound)
        # b:
        # '''
        # Map:
        # wwwwwwwwwwwwwwwwwwww
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000e0000fw
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # wwwwwwwwwwwwwwwwwwww
        # '''
        # food_row = 13
        # food_col = 18
        # world = World(food_row, food_col)
        # enemy = Enemy(world)
        # # enemy start at row 13 and col 13
        # enemy.position = (StationaryTile.DIMS[1] * 13,
        #                   StationaryTile.DIMS[0] * 13)
        # subworld = world.get_current_subworld(13, 13)
        # enemy.shortest_path = []

        # new_entering_new_subworld = enemy.entering_new_subworld
        # new_last_left_shortest_path = \
        #     subworld.left_bound[len(subworld.left_bound) / 2]
        # new_last_top_shortest_path = \
        #     subworld.top_bound[len(subworld.top_bound) / 2]
        # new_last_bot_shortest_path = \
        #     subworld.bot_bound[len(subworld.bot_bound) / 2]

        # enemy.do_something()

        # self.assertEqual(new_entering_new_subworld,
        #                  enemy.entering_new_subworld)
        # self.assertIn((enemy.shortest_path[-1].row,
        #                enemy.shortest_path[-1].col),
        #                [new_last_top_shortest_path,
        #                  new_last_bot_shortest_path,
        #                  new_last_left_shortest_path])
        # # c:
        # '''
        # Map:
        # wwwwwwwwwwwwwwwwwwww
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000f00000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000e00000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # wwwwwwwwwwwwwwwwwwww
        # '''
        # food_row = 7
        # food_col = 13
        # world = World(food_row, food_col)
        # enemy = Enemy(world)
        # # enemy start at row 13 and col 13
        # enemy.position = (StationaryTile.DIMS[1] * 13,
        #                   StationaryTile.DIMS[0] * 13)
        # subworld = world.get_current_subworld(13, 13)
        # enemy.shortest_path = []

        # new_entering_new_subworld = enemy.entering_new_subworld
        # new_last_right_shortest_path = \
        #     subworld.right_bound[len(subworld.right_bound) / 2]
        # new_last_left_shortest_path = \
        #     subworld.left_bound[len(subworld.left_bound) / 2]
        # new_last_bot_shortest_path = \
        #     subworld.bot_bound[len(subworld.bot_bound) / 2]

        # enemy.do_something()

        # self.assertEqual(new_entering_new_subworld,
        #                  enemy.entering_new_subworld)
        # self.assertIn((enemy.shortest_path[-1].row,
        #                enemy.shortest_path[-1].col),
        #                [new_last_right_shortest_path,
        #                  new_last_bot_shortest_path,
        #                  new_last_left_shortest_path])
        # # d:
        # '''
        # Map:
        # wwwwwwwwwwwwwwwwwwww
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000e0000fw
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # w000000000000000000w
        # wwwwwwwwwwwwwwwwwwww
        # '''
        # food_row = 18
        # food_col = 13
        # world = World(food_row, food_col)
        # enemy = Enemy(world)
        # # enemy start at row 13 and col 13
        # enemy.position = (StationaryTile.DIMS[1] * 13,
        #                   StationaryTile.DIMS[0] * 13)
        # subworld = world.get_current_subworld(13, 13)
        # enemy.shortest_path = []

        # new_entering_new_subworld = enemy.entering_new_subworld
        # new_last_right_shortest_path = \
        #     subworld.right_bound[len(subworld.right_bound) / 2]
        # new_last_left_shortest_path = \
        #     subworld.left_bound[len(subworld.left_bound) / 2]
        # new_last_top_shortest_path = \
        #     subworld.top_bound[len(subworld.top_bound) / 2]

        # enemy.do_something()

        # self.assertEqual(new_entering_new_subworld,
        #                  enemy.entering_new_subworld)
        # self.assertIn((enemy.shortest_path[-1].row,
        #                enemy.shortest_path[-1].col),
        #                [new_last_right_shortest_path,
        #                  new_last_top_shortest_path,
        #                  new_last_left_shortest_path])

if __name__ == '__main__':
    unittest.main()