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
spd = .2

# stars
star_path = join("images", "star.png")
star_surf = pg.image.load(star_path).convert_alpha()
stars = []

# meteor
meteor_path = join("images", "meteor.png")
meteor_surf = pg.image.load(meteor_path).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH * .5,WINDOW_HEIGHT * .5))

# laser
laser_path = join("images", "laser.png")
laser_surf = pg.image.load(laser_path).convert_alpha()
laser_padding = 20
laser_rect = laser_surf.get_frect(bottomright = (WINDOW_WIDTH - laser_padding, WINDOW_HEIGHT - laser_padding))


for i in range(20):
    x = randint(0, WINDOW_WIDTH-50)
    y = randint(0, WINDOW_HEIGHT-50)
    stars.append((x, y))

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.fill("darkgray")

    if player_rect.right > WINDOW_WIDTH:
        spd *= -1
    elif player_rect.left < 0:
        spd *= -1

    player_rect.left += spd 

    screen.blit(player_surf, player_rect)
    screen.blit(meteor_surf, meteor_rect)
    screen.blit(laser_surf, laser_rect)
    for i in range(len(stars)):
        screen.blit(star_surf, stars[i])

    pg.display.flip()

pg.quit()