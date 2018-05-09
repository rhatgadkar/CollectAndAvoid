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

if __name__ == '__main__':
    unittest.main()