# main game script controller:

# init
from scripts.__init__ import *
from scripts.restaurant import *

import pygame
import sys

if __name__ == '__main__':

    # Restaurant - agent of simulation, starting with waiters, tables and furnaces
    Ramen = Restaurant(1, 8, 2)

    #gamestates: 1 - simulation running, 0 - simulation finished
    gamestate = 1

    all_sprites = pygame.sprite.Group()

    # add sprites to draw to the list
    # Restaurant contains list of waiters, tables and furnaces
    for object in Ramen.space:
        all_sprites.add(object)

    # main game loop
    while gamestate != 0:  # the main game loop
        for event in pygame.event.get():
            if event.type == KEYUP:
                #control check for development purpose only
                #print(pygame.key.name(event.key))

                # list of events on keys:
                if event.key == K_RIGHT:
                    Ramen.Uber.move_right()
                elif event.key == K_LEFT:
                    Ramen.Uber.move_left()
                elif event.key == K_DOWN:
                    Ramen.Uber.move_down()
                elif event.key == K_UP:
                    Ramen.Uber.move_up()
                elif event.key == K_SPACE:
                    Ramen.Uber.next_round()
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