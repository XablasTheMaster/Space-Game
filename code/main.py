import pygame as pg
from os.path import join
from random import randint

# general setup
pg.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Space Shooter")

is_running = True

# importing the player image
player_path = join("images", "player.png")
player_surf = pg.image.load(player_path).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH * .5,WINDOW_HEIGHT * .5))
player_pos = [100, 150]

# stars
star_path = join("images", "star.png")
star_surf = pg.image.load(star_path).convert_alpha()
stars = []

for i in range(20):
    x = randint(0, WINDOW_WIDTH-50)
    y = randint(0, WINDOW_HEIGHT-50)
    stars.append((x, y))

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.fill("darkgray")
    player_rect.left += .2
    screen.blit(player_surf, player_rect)

    for i in range(len(stars)):
        screen.blit(star_surf, stars[i])

    pg.display.flip()

pg.quit()