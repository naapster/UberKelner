# main game script controller:

# init
from scripts.waiter import *
import sys
import pygame
from pygame.locals import *
import datetime


if __name__ == '__main__':

    # init list of variables, common for all simulations:
    # random coordinates
    random_coordinates = create_random_coordinates()
    # number of tables
    num_tables = 8
    # number of furnaces
    num_furnaces = 2

    # save state of simulation to file
    with open("simulation_log.txt", "a") as myfile:
        myfile.write(str(datetime.datetime.now()) + '\t' + str(num_tables) + '\t' +
                     str(num_furnaces) + '\t' + str(random_coordinates) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(random_coordinates, num_tables, num_furnaces)

    # list of all sprites for graphics window to draw
    all_sprites = pygame.sprite.Group()

    # add waiter to sprites list
    all_sprites.add(Uber)
    # add all tables and furnaces to sprites list
    for _ in Uber.restaurant.all_objects_to_list():
        all_sprites.add(_)

    # main game loop:
    # clear event log of game
    pygame.event.clear()
    # for eternity:
    while True:
        # wait for key pressed:
        for event in pygame.event.get():
            # if [x] in right upper corner was clicked, exit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # or after key was pressed:
            elif event.type == KEYUP:
                # exit simulation anyway:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # or run new round for environment
                Uber.next_round(event.key)
                # WARNING
                # in the future release, on key pressed no event key will be passed
                # and the waiter will have to choose the action on his own

        # simulation sprites control
        all_sprites.update()
        # draw background
        DISPLAYSURF.fill(WHITE)
        # draw sprites
        all_sprites.draw(DISPLAYSURF)
        # refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)