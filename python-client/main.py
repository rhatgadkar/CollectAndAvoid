from sys import exit
import pygame
import pygame.locals
from player import Player
from tile import Tile
from world import World
from keys import Keys

FPS = 60
BLACK = (0 ,0, 0)

screen = pygame.display.set_mode(World.SCREEN_DIMS)
clock = pygame.time.Clock()
world = World()
player = Player(world)

while 1:
    # user input
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_RIGHT:
                Keys.set_right()
            elif event.key == pygame.locals.K_LEFT:
                Keys.set_left()
            elif event.key == pygame.locals.K_UP:
                Keys.set_up()
            elif event.key == pygame.locals.K_DOWN:
                Keys.set_down()
            elif event.key == pygame.locals.K_ESCAPE:
                exit(0)

    # simulation
    player.do_something()
    if player.dead:
        print 'player dead'
        exit(0)

    # rendering
    screen.fill(BLACK)
    for row in range(world.num_total_rows):
        for col in range(world.num_total_cols):
            t = world.grid[row][col]
            if t == None:
                continue
            t_rect = pygame.Rect(t.position, Tile.DIMS)
            pygame.draw.rect(screen, t.color, t_rect)
    player_rect = pygame.Rect(player.position, Tile.DIMS)
    pygame.draw.rect(screen, player.color, player_rect)
    pygame.display.flip()
