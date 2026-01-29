import pygame as pg

# general setup
pg.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Space Game")
is_running = True

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.fill("cornflowerblue")
    pg.display.flip()

pg.quit()