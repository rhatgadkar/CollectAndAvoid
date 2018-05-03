from sys import exit
import pygame
import pygame.locals
from player import Player
from enemy import Enemy
from stationary_tile import StationaryTile
from moving_tile import MovingTile
from world import World
from keys import Keys
from random import randint

DEBUG_AI = False

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
enemy = None
game_started = False
text_surface = myfont.render("Press 'Enter' to start game.", False, WHITE)
game_paused = False

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
                        if food_row == Enemy.STARTING_ROW and \
                                food_col == Enemy.STARTING_COL:
                            continue
                        break
                    world = World(food_row, food_col)
                    if not DEBUG_AI:
                        player = Player(world)
                    enemy = Enemy(world)
                    Keys.reset()
                    if not DEBUG_AI:
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
                elif event.key == pygame.locals.K_p:
                    game_paused = not game_paused

    # simulation
    if game_paused:
        continue
    if game_started:
        enemy.do_something()
        if not DEBUG_AI:
            player.do_something()
            if player.dead:
                game_started = False
                text_surface = myfont.render(
                    "Game over. Press 'Enter' to start new game.", False,
                    WHITE)

    # rendering
    screen.fill(BLACK)
    if game_started:
        # draw stationary tiles:
        for row in range(World.TOTAL_ROWS):
            for col in range(World.TOTAL_COLS):
                t = world.grid[row][col]
                if t == None:
                    continue
                t_draw_position = (t.position[0],
                                   t.position[1] + TILE_Y_OFFSET)
                t_rect = pygame.Rect(t_draw_position, StationaryTile.DIMS)
                pygame.draw.rect(screen, t.color, t_rect)
        # draw player:
        if not DEBUG_AI:
            player_draw_position = (player.position[0],
                                    player.position[1] + TILE_Y_OFFSET)
            player_rect = pygame.Rect(player_draw_position, MovingTile.DIMS)
            pygame.draw.rect(screen, player.color, player_rect)
        # draw enemy:
        enemy_draw_position = (enemy.position[0],
                               enemy.position[1] + TILE_Y_OFFSET)
        enemy_rect = pygame.Rect(enemy_draw_position, MovingTile.DIMS)
        pygame.draw.rect(screen, enemy.color, enemy_rect)
        if not DEBUG_AI:
            score_surface = myfont.render('Score: %s' % str(player.score),
                                          False, WHITE)
            screen.blit(score_surface, (0, 0))
        # draw debug grids:
        if DEBUG_AI:
            pygame.draw.line(screen, WHITE, (100, 0 + TILE_Y_OFFSET),
                             (100, 400 + TILE_Y_OFFSET))
            pygame.draw.line(screen, WHITE, (200, 0 + TILE_Y_OFFSET),
                             (200, 400 + TILE_Y_OFFSET))
            pygame.draw.line(screen, WHITE, (300, 0 + TILE_Y_OFFSET),
                             (300, 400 + TILE_Y_OFFSET))
            pygame.draw.line(screen, WHITE, (0, 100 + TILE_Y_OFFSET),
                             (400, 100 + TILE_Y_OFFSET))
            pygame.draw.line(screen, WHITE, (0, 200 + TILE_Y_OFFSET),
                             (400, 200 + TILE_Y_OFFSET))
            pygame.draw.line(screen, WHITE, (0, 300 + TILE_Y_OFFSET),
                             (400, 300 + TILE_Y_OFFSET))
            for subworld in world.subworlds:
                for (row, col) in subworld.left_bound:
                    bound_draw_position = (col * StationaryTile.DIMS[0],
                                        row * StationaryTile.DIMS[1] +
                                        TILE_Y_OFFSET)
                    bound_rect = pygame.Rect(bound_draw_position,
                                            StationaryTile.DIMS)
                    pygame.draw.rect(screen, (255, 255, 0), bound_rect, 1)
                for (row, col) in subworld.right_bound:
                    bound_draw_position = (col * StationaryTile.DIMS[0],
                                        row * StationaryTile.DIMS[1] +
                                        TILE_Y_OFFSET)
                    bound_rect = pygame.Rect(bound_draw_position,
                                            StationaryTile.DIMS)
                    pygame.draw.rect(screen, (255, 255, 0), bound_rect, 1)
                for (row, col) in subworld.top_bound:
                    bound_draw_position = (col * StationaryTile.DIMS[0],
                                        row * StationaryTile.DIMS[1] +
                                        TILE_Y_OFFSET)
                    bound_rect = pygame.Rect(bound_draw_position,
                                            StationaryTile.DIMS)
                    pygame.draw.rect(screen, (255, 255, 0), bound_rect, 1)
                for (row, col) in subworld.bot_bound:
                    bound_draw_position = (col * StationaryTile.DIMS[0],
                                        row * StationaryTile.DIMS[1] +
                                        TILE_Y_OFFSET)
                    bound_rect = pygame.Rect(bound_draw_position,
                                            StationaryTile.DIMS)
                    pygame.draw.rect(screen, (255, 255, 0), bound_rect, 1)
    else:
        screen.blit(text_surface, (50, 50))
    pygame.display.flip()
