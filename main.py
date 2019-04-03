# main game script controller:

# init
from scripts.waiter import *
import sys
import pygame
import numpy as np
from pygame.locals import *
import datetime

def change(log):
    coordinates1 = []
    coordinates2 = []
    coordinates3 = []
    for i in log[4]:
        if i.isnumeric():
            coordinates1.append(i)
    coordinates3 = coordinates1[0::2]
    coordinates2 = coordinates1[1::2]
    result = np.array(list(zip(coordinates3,coordinates2)),dtype=np.int32)
    return result

if __name__ == '__main__':

    # init list of variables, common for all simulations:
    control = True

    if control:
        # reload simulation state from log:
        # get last row in log
        with open("simulation_log.txt") as myfile:
            log = list(myfile)[-1].split('\t')

        # size of simulation^2
        N = 5
        # number of tables
        num_tables = int(log[1])
        # number of furnaces
        num_furnaces = int(log[2])
        # number of walls
        num_walls = int(log[3])
        # random coordinates - REPAIR! how to parse string from log[4], looking like list, to list?
     #  coordinates = " ".join(map(str, log[4]))
       # coordinates = [[2, 0], [0, 4], [0, 0], [1, 0], [3, 0], [4, 0], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]]
      #  coordinates1 = np.loadtxt("simulation_log.txt", delimiter=',' , dtype=np.str)

        coordinates = change(log)





    else:

        # generate random simulation:
        # size of simulation^2
        N = 5
        # number of tables
        num_tables = 0
        # number of furnaces
        num_furnaces = 1
        # number of walls
        num_walls = 10
        # random coordinates
        coordinates = create_random_coordinates()

        # save state of simulation to file
        with open("simulation_log.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t' + str(num_tables) + '\t' + str(num_furnaces) + '\t' + str(num_walls)
                         + '\t' + str(coordinates[:(num_tables+num_furnaces+num_walls+1)]) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(coordinates, num_tables, num_furnaces, num_walls)

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