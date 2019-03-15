# main game script controller:

# init
from scripts.waiter import *

import pygame
import sys

if __name__ == '__main__':

    # Restaurant - agent of simulation, starting with waiters, tables and furnaces
    #Ramen = Restaurant(1, 8, 2)

    # init random coordinates
    random_coordinates = create_random_coordinates()

    # one special playable waiter
    Uber = Waiter(random_coordinates, 8, 2)

    #gamestates: 1 - simulation running, 0 - simulation finished
    gamestate = 1

    all_sprites = pygame.sprite.Group()

    # add sprites to draw to the list
    all_sprites.add(Uber)
    for table in Uber.dining_tables:
        all_sprites.add(table)
    for furnace in Uber.furnaces:
        all_sprites.add(furnace)

    # main game loop
    while gamestate != 0:  # the main game loop
        for event in pygame.event.get():
            if event.type == KEYUP:
                #control check for development purpose only
                #print(pygame.key.name(event.key))

                # list of events on keys:
                if event.key == K_RIGHT:
                    Uber.move_right()
                elif event.key == K_LEFT:
                    Uber.move_left()
                elif event.key == K_DOWN:
                    Uber.move_down()
                elif event.key == K_UP:
                    Uber.move_up()
                elif event.key == K_SPACE:
                    Uber.next_round()
                elif event.key == K_ESCAPE:
                    gamestate = 0
                elif event.key == K_r:
                    gamestate = -1
                    while gamestate == -1:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                gamestate = 0
                            elif event.type == KEYUP:
                                if event.key == K_r:
                                    gamestate = 1

        # simulation sprites control - to be added
        all_sprites.update()
        # draw background
        DISPLAYSURF.fill(WHITE)
        # draw sprites
        all_sprites.draw(DISPLAYSURF)
        # Refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)

    # end of main loop: close simulation
    pygame.quit()
    sys.exit()