# simulation controller:

from scripts.waiter import *
from random import shuffle
import sys
# solve pygame audio driver error
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from pygame.locals import *
import datetime

# filename __init__ is required to treat scripts folder as resource
# variables:
# size of sprites in px
blocksize = 60


# init sprite sprite_name on coordinate x, y
def init_graphics(self, x, y, sprite_name):
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # init graphics - do not touch!
    pygame.sprite.Sprite.__init__(self)
    # set image
    self.image = pygame.image.load("images/" + sprite_name + ".png")
    # resize image to blocksize
    self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
    # set coordinates
    self.rect = self.image.get_rect()
    self.rect.x = x * blocksize
    self.rect.y = y * blocksize
    # //////////////////////////////////////////////////


# generate random positions list for all objects
def create_random_coordinates():
    # list of all possible numbers of coordinate
    _ = range(N)
    # cartesian product of all possible numbers
    matrix_fields = [[posX, posY] for posX in _ for posY in _]
    # randomize order of coordinates
    shuffle(matrix_fields)
    return matrix_fields


if __name__ == '__main__':

    # init list of variables, common for all simulations:

    # frames per second setting
    FPS = 30

    # choose whether to run simulation from log (True) or generate random (False)
    control = True

    run_simulation = -1  # index of simulation to run in log list

    if control:
        # reload simulation state from log:
        # get last row in log
        with open("simulation_log.txt") as myfile:
            log = list(myfile)[run_simulation].split('\t')

        # amount of blocks in row of simulation - not currently active, change init
        N = int(log[1])
        # number of tables
        num_tables = int(log[2])
        # number of furnaces
        num_furnaces = int(log[3])
        # number of walls
        num_walls = int(log[4])
        # random coordinates
        # backup: [[2, 0], [0, 4], [0, 0], [1, 0], [3, 0], [4, 0], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]]
        _ = log[5].replace('[', '').split('],')
        coordinates = [list(map(int, s.replace(']', '').split(','))) for s in _]

    else:

        # generate random simulation:
        # amount of blocks in row of simulation - not currently active, change init
        N = 5
        # number of tables
        num_tables = 0
        # number of furnaces
        num_furnaces = 1
        # number of walls
        num_walls = 10
        # random coordinates
        coordinates = create_random_coordinates()[:(num_tables + num_furnaces + num_walls + 1)]

        # save state of simulation to file
        with open("simulation_log.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t'
                         + str(N) + '\t' + str(num_tables) + '\t' + str(num_furnaces) + '\t' + str(num_walls) + '\t'
                         + str(coordinates[:(num_tables+num_furnaces+num_walls+1)]) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(N, coordinates, num_tables, num_furnaces, num_walls)

    # list of all sprites for graphics window to draw
    all_sprites = pygame.sprite.Group()

    # add waiter to sprites list
    all_sprites.add(Uber)
    # add all tables and furnaces to sprites list
    for _ in Uber.restaurant.all_objects_to_list():
        all_sprites.add(_)

    # main game loop:

    # graphics init
    pygame.init()
    fpsClock = pygame.time.Clock()
    # set up the window
    DISPLAYSURF = pygame.display.set_mode((blocksize * N, blocksize * N), 0, 32)
    pygame.display.set_caption('UberKelner')
    WHITE = (255, 255, 255)

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
