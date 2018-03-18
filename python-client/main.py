from sys import exit
import pygame
import pygame.locals
from player import Player
from tile import Tile
from world import World
from keys import Keys
from random import randint

FPS = 60
BLACK = (0 ,0, 0)
WHITE = (255, 255, 255)
TILE_Y_OFFSET = 50
SCREEN_DIMS = (World.WORLD_DIMS[0], World.WORLD_DIMS[1] + TILE_Y_OFFSET)

screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 16)
clock = pygame.time.Clock()
world = None
player = None
game_started = False
text_surface = myfont.render("Press 'Enter' to start game.", False, WHITE)

while True:
    # user input
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN:
            if not game_started:
                if event.key == pygame.locals.K_RETURN:
                    game_started = True
                    while True:
                        food_row = randint(1, World.TOTAL_ROWS - 2)
                        food_col = randint(1, World.TOTAL_COLS - 2)
                        if food_row == Player.STARTING_ROW and \
                                food_col == Player.STARTING_COL:
                            continue
                        break
                    world = World(food_row, food_col)
                    player = Player(world)
                    Keys.reset()
                    player.dead = False
                elif event.key == pygame.locals.K_ESCAPE:
                    exit(0)
            else:
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
    if game_started:
        player.do_something()
        if player.dead:
            game_started = False
            text_surface = myfont.render(
                "Game over. Press 'Enter' to start new game.", False, WHITE)

    # rendering
    screen.fill(BLACK)
    if game_started:
        for row in range(World.TOTAL_ROWS):
            for col in range(World.TOTAL_COLS):
                t = world.grid[row][col]
                if t == None:
                    continue
                t_draw_position = (t.position[0],
                                   t.position[1] + TILE_Y_OFFSET)
                t_rect = pygame.Rect(t_draw_position, Tile.DIMS)
                pygame.draw.rect(screen, t.color, t_rect)
        player_draw_position = (player.position[0],
                                player.position[1] + TILE_Y_OFFSET)
        player_rect = pygame.Rect(player_draw_position, Tile.DIMS)
        pygame.draw.rect(screen, player.color, player_rect)
        score_surface = myfont.render('Score: %s' % str(player.score), False,
                                      WHITE)
        screen.blit(score_surface, (0, 0))
    else:
        screen.blit(text_surface, (50, 50))
    pygame.display.flip()
