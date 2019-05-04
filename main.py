#!/usr/bin/python
# -*- coding: utf-8 -*-

# simulation controller:

import datetime
import os
from os import path
from random import shuffle
from argparse import ArgumentParser
import pygame
from pygame.locals import *
from scripts.waiter import *

# solve pygame audio driver error
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# filename __init__ is required to treat scripts folder as resource
# variables:
# size of sprites in px
blocksize = 60
# sprite constants
SPRITE_FOLDER = 'images'
SPRITE_EXTENSION = '.png'


# init sprite sprite_name on coordinate x, y
def init_graphics(self, x, y, sprite_name):
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # init graphics - do not touch!
    pygame.sprite.Sprite.__init__(self)
    # set image
    self.image = pygame.image.load(path.join(SPRITE_FOLDER, sprite_name + SPRITE_EXTENSION))
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
    print("Main: simulation controller executed...")

    # parse arguments
    print("Main: Parsing arguments")
    description = "Project UberKelner\n Project goal: to create a static discrete environment corresponding " \
                  "to the real restaurant and the artificial intelligence agent serving as a waiter in the restaurant."
    parser = ArgumentParser(description=description)
    # --size 10
    parser.add_argument("-n", "--size", help="set size of simulation", required=False, default=10)
    # --fps 30
    parser.add_argument("-f", "--fps", help="set frames per second of simulation", required=False, default=30)
    # --control True
    parser.add_argument("-c", "--control", help="choose whether to run simulation from log or random",
                        required=False, default=True)
    # --random N num_tables num_furnaces num_walls
    parser.add_argument("-r", "--random", help="create random simulation with parameters: "
                                               "N num_tables num_furnaces num_walls", required=False, default=False)
    # --log -1
    parser.add_argument("-l", "--log", help="run simulation from log", required=False, default=-1)
    # --solution depthfs/breathfs/bestfs/all
    parser.add_argument("-s", "--solution",
                        help="choose solving method.\nMethods available: depthfs, breathfs, bestfs, all. "
                             "Deep-first search is the default choice.", required=False, default="depthfs")
    # --blocksize 60
    parser.add_argument("-b", "--blocksize", help="set size of sprites (in px)", required=False, default=60)

    # args will be a dictionary containing the arguments
    args = vars(parser.parse_args())

    # init list of variables, common for all simulations:
    # amount of blocks in row of simulation
    N = args['size']
    FPS = args['fps']
    control = args['control']
    # row in simulation log to load - coordinates like in list, negative numbers mean positipon from the back of list
    run_simulation = args['log']
    solution = args['solution']
    blocksize = args['blocksize']

    print("Args: Set size to %s" % N)
    print("Args: Set FPS to %s" % FPS)
    print("Args: Set control to %s" % control)
    print("Args: Set simulation log to %s" % run_simulation)
    print("Args: Set solution to %s" % args['solution'])
    print("Args: Set blocksize to %s" % args['blocksize'])

    # default settings
    # number of tables
    num_tables = 0
    # number of furnaces
    num_furnaces = 1
    # number of walls
    num_walls = 10

    '''
    # choose whether to run simulation from log (True) or generate random (False)
    if args['random']:
        print("Args: Generating random simulation")
        control = False
    else:
        if args['log']:
            print("Args: Generating simulation from %s log" % args['log'])
            control = True
            run_simulation = args['log']  # index of simulation to run in log list
        else:
            print("Main: log loig")
    '''

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
        _ = log[5].replace('[', '').split('],')
        coordinates = [list(map(int, s.replace(']', '').split(','))) for s in _]

    else:

        # generate random simulation:
        # random coordinates
        coordinates = create_random_coordinates()[:(num_tables + num_furnaces + num_walls + 1)]
        # rest of values are default

        # save state of simulation to file
        with open("simulation_log.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + '\t'
                         + str(N) + '\t' + str(num_tables) + '\t' + str(num_furnaces) + '\t' + str(num_walls) + '\t'
                         + str(coordinates[:(num_tables + num_furnaces + num_walls + 1)]) + '\n')

    # waiters - agents of simulation, owning matrices of restaurants
    # one special playable waiter
    Uber = Waiter(N, coordinates, num_tables, num_furnaces, num_walls, solution)

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
    control = True
    while control:
        # wait for key pressed:
        for event in pygame.event.get():
            # if [x] in right upper corner was clicked, exit game
            if event.type == QUIT:
                control = False
            # or after key was pressed:
            elif event.type == KEYUP:
                # exit simulation anyway:
                if event.key == K_ESCAPE:
                    control = False
                # or run new round for environment
                Uber.next_round(event.key)

        # simulation sprites control
        all_sprites.update()
        # draw background
        DISPLAYSURF.fill(WHITE)
        # draw sprites
        all_sprites.draw(DISPLAYSURF)
        # refresh Screen
        pygame.display.flip()
        fpsClock.tick(FPS)

    print("Main: simulation controller execution complete.")
    pygame.quit()
    sys.exit()
